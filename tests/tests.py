from src.masks import mask_account, mask_card, convert_date

try:
    print(mask_card("7000792289606361"))
except ValueError:
    print("Имеется ошибка, пересмотрите данные")
else:
    print("Все успешно! Маска карты выполнена")

try:
    print(mask_account("73654108430135874305"))
except IndexError:
    print("Имеется ошибка, пересмотрите данные")
else:
    print("Все успешно! Маска аккаунта выполнена")

print(convert_date("2018-07-11T02:26:18.671407"))