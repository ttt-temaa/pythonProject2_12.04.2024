import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions,currency,expected",
    [
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        (
            [{"operationAmount": {"currency": {"code": "RUB"}}}],
            "RUB",
            [{"operationAmount": {"currency": {"code": "RUB"}}}],
        ),
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "RUB"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions: list, currency: str, expected: list) -> None:
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert filtered_transactions == expected


@pytest.mark.parametrize(
    "transactions,expected",
    [
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        ([{"description": "Перевод со счета на счет"}], ["Перевод со счета на счет"]),
        ([{"description": "Перевод с карты на карту"}], ["Перевод с карты на карту"]),
    ],
)
def test_transaction_descriptions(transactions: list[dict], expected: list) -> None:
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected


def test_card_number_generator() -> None:
    numbers = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert numbers == ["".join(exp.split()) for exp in expected]
