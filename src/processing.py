import re
from collections import Counter

# Функция принимающая список и на выходе получаем список с нужным ключом
def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    На выходе получаем новый список"""
    new_list_dict = []
    # Проверяем есть такой ключ у нас в словаре
    for item in list_dict:
        if item.get("state") == state:
            new_list_dict.append(item)
    return new_list_dict


# Функция, которая сортирует по дате словари
def sort_by_date(list_dict: list, sorting: bool = True) -> list:
    """Функция принимает список словарей и сортирует по умолчанию - убыванию."""
    # Сортируем список по ключу date
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=sorting)
    return sorted_list


def search_by_string(list_dict: list, pattern: str) -> list:
    new_list =[]
    for transaction in list_dict:
        if transaction.get('description'):
            if re.search(pattern, transaction.get('description')):
                new_list.append(transaction)
    return new_list


def category_count(list_dict: list, category_list: list):
    category = [transaction.get('description') for transaction in list_dict]
    result = Counter(category)
    if category_list:
        return {cat: result.get(cat, 0) for cat in category_list}
    return result

