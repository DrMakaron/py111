from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # TODO реализовать алгоритм сортировки подсчетами
    output = [0] * len(container)
    freq = [0] * (len(container) + 1)

    for i in container:
        freq[i] = freq[i] + 1

    total = 0
    for i in range(len(container) + 1):
        count = freq[i]
        freq[i] = total
        total += count

    for i in container:
        output[freq[i]] = i
        freq[i] = freq[i] + 1

    for i in range(len(container)):
        container[i] = output[i]

    return container
