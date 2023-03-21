def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError

    factorial = 1

    for i in range(2, n + 1):
        factorial *= i

    return factorial
