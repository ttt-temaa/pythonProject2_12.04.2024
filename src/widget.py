from src.masks import mask_account, mask_card


def convert_date(input_date: str) -> str:
    """Конвертация даты"""
    try:
        date_obj = input_date[8:10] + "." + input_date[5:7] + "." + input_date[:4]

        return date_obj
    except ValueError:
        return "Некорректный формат даты"


def transform_data(input_data: str) -> str:
    """Возвращает исходную строку с замаскированным номером карты/счета."""
    number = "".join([num for num in input_data if num.isdigit()])
    name = "".join([word for word in input_data if word.isalpha() or word == " "]).strip()
    if name != "Счет":
        transformed_card_number = mask_card(number)
        return f"{name} {transformed_card_number}"
    elif "Счет" == name:
        transformed_account_number = mask_account(number)
        return f"{name} {transformed_account_number}"
    else:
        return "Не удалось распознать тип данных"
