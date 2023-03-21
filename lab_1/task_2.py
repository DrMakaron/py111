def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    # TODO реализовать проверку скобочной группы
    opened_brackets = ('(', '[', '{')
    closed_brackets = (')', ']', '}')
    stack = []

    for char in brackets_row:
        if char in opened_brackets:
            stack.append(char)
        if char in closed_brackets:
            if not stack:
                return False
            index = closed_brackets.index(char)
            open_bracket = opened_brackets[index]
            if stack[-1] == open_bracket:
                stack.pop()
            else:
                return False

    return not stack


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
