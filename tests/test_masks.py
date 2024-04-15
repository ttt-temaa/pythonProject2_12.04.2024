import pytest

from src.masks import mask_account, mask_card


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
