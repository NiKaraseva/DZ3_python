# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите десятичное число: '))

result = []

while number > 0:
    result.append(number % 2)
    number //= 2

result.reverse()
print(*result)