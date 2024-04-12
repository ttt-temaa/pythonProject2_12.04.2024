def filter_by_state(data, state='EXECUTED'):
    """
    Функция фильтрует список словарей по ключу 'state', возвращая новый список,
    содержащий только те словари, у которых 'state' соответствует переданному значению.

    :data: Список словарей, который нужно отфильтровать.
    :state: Значение для ключа 'state'. Если не указано, используется 'EXECUTED'.
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data if item['state'] == state]

input_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_data_executed = filter_by_state(input_data)
filtered_data_canceled = filter_by_state(input_data, 'CANCELED')