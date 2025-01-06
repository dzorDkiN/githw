from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [entry for entry in data if entry.get("state") == state]


# Пример использования:
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

result = filter_by_state(data)
print(result)


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(str(x["date"])), reverse=descending)


# Пример использования
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sorted_data_desc = sort_by_date(data)  # Сортировка по убыванию (по умолчанию)
print("Сортировка по убыванию:", sorted_data_desc)

sorted_data_asc = sort_by_date(data, descending=False)  # Сортировка по возрастанию
print("Сортировка по возрастанию:", sorted_data_asc)
