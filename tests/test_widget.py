import pytest

from src.widget import convert_date, transform_data


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
