import json
import os
from typing import Any, Dict, List
from dotenv import load_dotenv
import requests


def read_operations_file(path: str) -> List[Dict[str, Any]]:
    """
    Возвращает список словарей с данными о финансовых транзакциях из JSON-файла.

    :param path: Путь до JSON-файла с транзакциями.
    :return: Список словарей с данными о транзакциях.
    """
    try:
        with open(path, "r", encoding="UTF8") as file:
            ret = json.load(file)
            return ret
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []


load_dotenv()
API_KEY = os.getenv('API_KEY')


def convert_currency(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях, конвертируя её из другой валюты при необходимости.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    if transaction["operationAmount"]["currency"]["code"] == "USD":
        # Здесь должен быть код для обращения к API для получения курса доллара
        # Предположим, что курс доллара можно получить так:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD")
        rate = response.json()["conversion_rates"]["RUB"]
        amount = float(transaction["operationAmount"]["amount"]) * rate
    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        # Аналогично для евро:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR")
        rate = response.json()["conversion_rates"]["RUB"]
        amount = float(transaction["operationAmount"]["amount"]) * rate
    else:
        # Если валюта транзакции другая или неизвестна, возвращаем сумму без изменений
        amount = float(transaction["operationAmount"]["amount"])
    return amount
