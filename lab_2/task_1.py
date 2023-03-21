"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError

    min_elem = arr[0]
    min_elem_index = 0

    for i in range(len(arr)):
        if arr[i] < min_elem:
            min_elem = arr[i]
            min_elem_index = i

    return min_elem_index
