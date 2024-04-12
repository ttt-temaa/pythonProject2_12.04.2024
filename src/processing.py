def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция фильтрует список словарей по ключу 'state', возвращая новый список,
    содержащий только те словари, у которых 'state' соответствует переданному значению.

    :data: Список словарей, который нужно отфильтровать.
    :state: Значение для ключа 'state'. Если не указано, используется 'EXECUTED'.
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data if item["state"] == state]


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filtered_data_executed = filter_by_state(input_data)
filtered_data_canceled = filter_by_state(input_data, "CANCELED")


def sort_dicts_by_date(data: list, descending: bool = True) -> list:
    """
    Функция сортирует список словарей по дате (ключ 'date'), может принимать необязательный аргумент для задания
    порядка сортировки (по убыванию или возрастанию).

    :data: Список словарей, который нужно отсортировать.
    :
    descending: Логический флаг, указывающий на то, что сортировка должна быть выполнена по убыванию (True) или по
     возрастанию (False).
    :return: Отсортированный список словарей.
    """
    sorted_data = sorted(data, key=lambda x: (x["date"], "%Y-%m-%dT%H:%M:%S.%f"))

    if descending:
        sorted_data.reverse()

    return sorted_data


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sorted_descending = sort_dicts_by_date(input_data, True)
sorted_ascending = sort_dicts_by_date(input_data, False)
