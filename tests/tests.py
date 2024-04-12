from src.masks import mask_account, mask_card
from src.processing import filtered_data_canceled, filtered_data_executed, sorted_ascending, sorted_descending
from src.widget import convert_date, transform_data

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
print(transform_data("Visa Platinum 7000 7922 8960 6361"))
print(transform_data("Счет 73654108430135874305"))

print(filtered_data_executed)
print(filtered_data_canceled)

print(sorted_descending)
print(sorted_ascending)
