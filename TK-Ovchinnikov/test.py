from app import get_mark

# Positive test
print(get_mark(1, 1, 1, 1) == 2)
print(get_mark(1, 2, 3, 4) == 2)

# Negative test
print(get_mark(-1, 1, 1, 1) == "За первое задание минимум 0 балов")
print(get_mark("1", 1, 1, 1) == "Первое число не является цифрой")
print(get_mark(11, 1, 1, 1) == "За первое задание максимум 10 балов")
