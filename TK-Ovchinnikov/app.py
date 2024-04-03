def get_mark(task1: int, task2: int, task3: int, task4: int) -> int:
    if not isinstance(task1, int):
        return "Первое число не является цифрой"
    if not isinstance(task2, int):
        return "Второе число не является цифрой"
    if not isinstance(task3, int):
        return "Третье число не является цифрой"
    if not isinstance(task4, int):
        return "Четвертое число не является цифрой"

    if task1 > 10:
        return "За первое задание максимум 10 балов"
    if task2 > 50:
        return "За второе задание максимум 50 балов"
    if task3 > 30:
        return "За третье задание максимум 30 балов"
    if task4 > 10:
        return "За четвертое задание максимум 10 балов"

    if task1 < 0:
        return "За первое задание минимум 0 балов"
    if task2 < 0:
        return "За второе задание минимум 0 балов"
    if task3 < 0:
        return "За третье задание минимум 0 балов"
    if task4 < 0:
        return "За четвертое задание минимум 0 балов"

    balls_sum = sum([task1, task2, task3, task4])

    if balls_sum < 20:
        return 2
    if balls_sum < 40:
        return 3
    if balls_sum < 70:
        return 4
    return 5


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    print(get_mark(n1, n2, n3, n4))
