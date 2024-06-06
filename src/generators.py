import itertools
from typing import Iterator, List


def filter_by_currency(transactions: List[dict], currency: str) -> list[dict]:
    """
    Генератор, который фильтрует транзакции по указанной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency: Код валюты, по которому нужно фильтровать.
    :return: Итератор, который выдает транзакции с заданной валютой.
    """
    # Фильтрация транзакций по валюте
    filtered_transactions = []

    for transaction in transactions:
        if "operationAmount" in transaction and transaction["operationAmount"]["currency"]["code"] == currency:
            filtered_transactions.append(transaction)
        elif "currency_code" in transaction and transaction["currency_code"] == currency:
            filtered_transactions.append(transaction)

    return filtered_transactions


def transaction_descriptions(transactions: List[dict]) -> Iterator[str]:
    """
    Генератор, который выдает описание каждой транзакции.

    :param transactions: Список словарей с транзакциями.
    :return: Итератор, который выдает описание каждой транзакции.
    """
    # Возвращаем итератор, который выдает описание каждой транзакции
    return (transaction["description"] for transaction in transactions)


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт.

    start: Начальный номер карты.
    end: Конечный номер карты.
    return: Итератор, который генерирует номера карт в заданном диапазоне.
    """
    # Генерация номеров карт в первичном диапазоне
    for number in itertools.count(start, step=1):
        if number > end:
            break
        yield f"{number:0>16}"
