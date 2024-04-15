import pytest

from src.masks import mask_account, mask_card
from src.processing import filter_by_state, sort_dicts_by_date
from src.widget import convert_date, transform_data


@pytest.mark.parametrize(
    "card_number,expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234567890123457", "1234 56** **** 3457"),
        ("1234567890123458", "1234 56** **** 3458"),
        ("1234567890123459", "1234 56** **** 3459"),
        ("1234567890123460", "1234 56** **** 3460"),
    ],
)
def test_mask_card(card_number: str, expected: str) -> None:
    actual = mask_card(card_number)
    assert actual == expected


@pytest.mark.parametrize(
    "input_date,expected",
    [
        ("2023-01-01T00:00:00.000000", "01.01.2023"),
        ("2022-12-31T23:59:59.999999", "31.12.2022"),
        ("2023-02-28T00:00:00.000000", "28.02.2023"),
        ("2023-02-28T23:59:59.999999", "28.02.2023"),
        ("2023-03-31T00:00:00.000000", "31.03.2023"),
        ("2023-03-31T23:59:59.999999", "31.03.2023"),
    ],
)
def test_convert_date(input_date: str, expected: str) -> None:
    actual = convert_date(input_date)
    assert actual == expected


@pytest.mark.parametrize(
    "account_number,expected",
    [
        ("1234567890", "**7890"),
        ("12345678901", "**8901"),
        ("123456789012", "**9012"),
        ("1234567890123", "**0123"),
        ("12345678901234", "**1234"),
    ],
)
def test_mask_account(account_number: str, expected: str) -> None:
    actual = mask_account(account_number)
    assert actual == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        ("Счет 1234567890", "Счет **7890"),
        ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),
        ("Неизвестный 1234567890123456", "Неизвестный 1234 56** **** 3456"),
    ],
)
def test_transform_data(input_data: str, expected: str) -> None:
    actual = transform_data(input_data)
    assert actual == expected


@pytest.fixture
def input_data() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(input_data: list) -> None:
    filtered_data_executed = filter_by_state(input_data)
    assert filtered_data_executed == input_data[:2]

    filtered_data_canceled = filter_by_state(input_data, "CANCELED")
    assert filtered_data_canceled == input_data[2:]


def test_sort_dicts_by_date(input_data: list) -> None:
    sorted_descending = sort_dicts_by_date(input_data, True)
    assert sorted_descending == sorted(input_data, key=lambda x: (x["date"], "%Y-%m-%dT%H:%M:%S.%f"))[::-1]

    sorted_ascending = sort_dicts_by_date(input_data, False)
    assert sorted_ascending == sorted(input_data, key=lambda x: (x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
