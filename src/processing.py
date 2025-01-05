def filter_by_state(state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param state: Значение, по которому будет производиться фильтрация. По умолчанию 'EXECUTED'.
    :return: Новый список словарей, удовлетворяющих условию
    """
    # Список данных
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    # Фильтрация данных по состоянию 'state'
    filtered_data = [entry for entry in data if entry.get('state') == state]

    # Возвращаем отфильтрованный список
    return filtered_data


# Пример использования
filtered_data = filter_by_state()  # По умолчанию фильтруем по состоянию 'EXECUTED'
print(filtered_data)

filtered_data_canceled = filter_by_state('CANCELED')  # Фильтруем по состоянию 'CANCELED'
print(filtered_data_canceled)


def sort_by_date(data=None, descending=True):
    """
    Сортирует список словарей по дате.

    :param data: Список словарей, содержащих ключ 'date'. Если не передан, используется стандартный список.
    :param descending: Если True, сортировка по убыванию (по умолчанию). Если False, сортировка по возрастанию.
    :return: Отсортированный список словарей.
    """
    # Если данные не переданы, используем примерный список
    if data is None:
        data = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

    # Сортировка по ключу 'date'
    return sorted(data, key=lambda x: x['date'], reverse=descending)


# Пример использования
sorted_data_desc = sort_by_date()  # Сортировка по убыванию (по умолчанию)
print("Сортировка по убыванию:", sorted_data_desc)

sorted_data_asc = sort_by_date(descending=False)  # Сортировка по возрастанию
print("Сортировка по возрастанию:", sorted_data_asc)
