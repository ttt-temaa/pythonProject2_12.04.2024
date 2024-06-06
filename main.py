import os
import re
from typing import Any, Dict, List

from src.funk_currency import search_transactions
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_dicts_by_date
from src.utils import read_operations_file, unpacking_csv_file, unpacking_excel_file
from src.widget import convert_date, transform_data


def choose_file_format() -> tuple[List[Dict], str]:
    """Запрашивает у пользователя формат файла и возвращает данные транзакций и тип файла."""

    f = input("""Привет! Добро пожаловать в программу работы с банковскими транзакициями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла\n""")
    if f == "1":
        print("Для обработки выбран json файл.\n")
        return read_operations_file(os.path.join("data/operations.json")), "json"
    elif f == "2":
        print("Для обработки выбран csv файл.\n")
        return unpacking_csv_file("data/transactions.csv"), "csv"
    elif f == "3":
        print("Для обработки выбран excel файл.\n")
        return unpacking_excel_file("data/transactions_excel.xlsx"), "excel"
    else:
        """Если выбрал не от 1 до 3 возращает обратно к началу работы программы """
        print("Пожалуйста, выберите - 1 или 2 или 3.")
        return choose_file_format()


def filter_by_statusw(data: List[Dict]) -> List[Dict]:
    """Фильтрует список транзакций по заданному статусу."""

    print("Выберите статус, по которому необходимо выполнить фильтрацию.")
    status = input("Доступные статусы: EXECUTED, CANCELED, PENDING\n")

    if status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        """Если выбрал некорректный статус возращает обратно к вопросу status"""
        print("Ошибка. Попробуйте еше раз).")
        return filter_by_statusw(data)

    return filter_by_state(data, status)


def sort_by_date_currency(data: List[Dict], file_type: str) -> list[dict[Any, Any]]:
    """Сортирует список транзакций по дате и фильтрует по валюте."""

    sort = input("Отсортировать операции по дате? \nВыберите ответ: ДА или НЕТ \n")
    if sort.lower() == "нет":
        pass
    elif sort.lower() == "да":

        time = input("По возрастанию или по убыванию? \nВыберите ответ: по возрастанию или по убыванию\n")
        if time.lower() == "по возрастанию":
            data = sort_dicts_by_date(data)
        elif time.lower() == "по убыванию":
            data = sort_dicts_by_date(data, False)
        else:
            """Если выбрал некорректное значение возращает обратно к вопросу sort"""
            print("Ошибка. Попробуйте еше раз).")
            return sort_by_date_currency(data, file_type)
    else:
        print("Некорректный ввод. Поробуйте ещё раз")
        return sort_by_date_currency(data, file_type)

    """Следующий шаг"""
    sort = input("Выводить только рублевые транзакции? \nВыберите ответ: ДА или НЕТ \n")
    if sort.lower() == "да":
        return filter_by_currency(data, "RUB")
    elif sort.lower() == "нет":
        return data
    else:
        """Если выбрал некорректный ответ возращает обратно к вопросу sort"""
        print("Неверное значение. Впишите, пожалуйста, корректный ответ")
        return sort_by_date_currency(data, file_type)


def filter_by_keyword(data: List[Dict]) -> List[Dict]:
    """Фильтрует список транзакций по ключевому слову в описании."""

    sort = input("Отсортировать список операций по определённому слову в описании? \nВыберите ответ: ДА или НЕТ \n")
    if sort.lower() == "да":
        to_find = input("По какому слову вы хотели бы найти? \n")
        return search_transactions(data, to_find)
    elif sort.lower() == "нет":
        return data
    else:
        """Если выбрал некорректное ответ возращает обратно к вопросу to_sort"""
        print("Попробуйте ещё раз. Программа не распознала ваш ответ.")
        return filter_by_keyword(data)


def console_transactions(data: List[Dict]) -> None:
    """Выводит отформатированный список транзакций."""

    print("Подведем итог транзакций, подходящие под ваши критерии")
    if data and len(data) != 0:
        print(f"Всего операций было: {len(data)}\n")
        for operation in data:
            print(convert_date(operation["date"]),
                  next(transaction_descriptions(data)),
                  )
            if re.search("Перевод", operation["description"]):
                print(transform_data(operation["from"]), " -> ", transform_data(operation["to"]))
            else:
                print(transform_data(operation["to"]))

            if "operationAmount" in operation:
                print(f"Сумма: {operation['operationAmount']['amount']}руб. \n")
            else:
                print(f"Сумма: {operation['amount']}руб. \n")
    else:
        """При условии, что не найдено того, что хотел пользователь"""
        print("Извините, не найдено ни одной транзакции подходящей под ваши критерии.")


def main() -> None:
    """Главная функция программы."""

    data, file_type = choose_file_format()
    data = filter_by_statusw(data)
    data = sort_by_date_currency(data, file_type)
    data = filter_by_keyword(data)
    console_transactions(data)


if __name__ == "__main__":
    main()
