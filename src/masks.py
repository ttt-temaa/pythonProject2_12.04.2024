def mask_card(card_number: str) -> str:
    """Возвращает маску номера карты"""
    # Разбиваем номер карты на блоки по 4 цифры
    card_mask = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
    # Заменяем центральные две цифры на звездочки
    card_mask = card_mask[:7] + "** **** " + card_mask[-4:]
    return card_mask


def mask_account(account_number: str) -> str:
    """Возвращает маску номера счета"""
    # Возвращаем номер счета, где последние 4 цифры заменены на звездочки
    account_mask = "**" + account_number[-4:]
    return account_mask
