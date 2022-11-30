# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
from decimal import Decimal

size = int(input('Введите размер списка: '))

my_list = []

for i in range(size):
    my_list.append(round((random.uniform(0.25, 10.25)), random.randint(0, 5)))
print(*my_list)

new_list = []

for i in range(len(my_list)):
    new_list.append(Decimal(str(my_list[i])) % 1)
print(*new_list)

max = new_list[0]
min = new_list[0]
for i in range(len(new_list)):
    if new_list[i] > max:
        max = new_list[i]
    if new_list[i] != 0 and new_list[i] < min:
        min = new_list[i]

print(f'Дробная часть {max} – максимальная')
print(f'Дробная часть {min} – минимальная')
print(f'Разница между максимальным и минимальным значением дробной части элементов = {max - min}')