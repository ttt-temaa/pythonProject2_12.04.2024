import json
import pytest
from unittest.mock import MagicMock, patch, Mock
from typing import Any, Dict, List
import os.path

import requests
from dotenv import load_dotenv

from src.utils import read_operations_file, convert_currency


# Функция для тестирования чтения файла
def test_read_operations_files() -> None:
    transactions = read_operations_file(os.path.join("..", "data", "operations.json"))
    assert isinstance(transactions, list)
    assert all(isinstance(t, dict) for t in transactions)


# Тесты для функции read_operations_file
@patch('builtins.open')
def test_read_operations_file(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }])
    assert read_operations_file(os.path.join("..", "data", "operations.json")) == [{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }]

def test_read_operations_file_error_path():
    assert read_operations_file("..\\data\\operatio.json") == []
    # Тесты для функции convert_currency


load_dotenv()
API_KEY = os.getenv('API_KEY')


@pytest.mark.parametrize("currency, price", (["USD", 90], ["EUR", 110]))
@patch('requests.get')
def test_convert_currency_eur_usd(mock_get, currency, price):
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": price}}
    assert convert_currency({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": currency
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }) == 31957.58 * price
    mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}")


def test_convert_currency_rub():
    assert convert_currency({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }) == 31957.58
