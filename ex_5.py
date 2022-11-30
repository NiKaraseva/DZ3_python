# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число: '))

def Fibonacci(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    else:
        return Fibonacci(x - 1) + Fibonacci(x - 2)

my_list = []

for i in range(number + 1):
    my_list.append(Fibonacci(i))
    my_list.insert(0, Fibonacci(i)*((-1)**(i + 1)))

print(*my_list)

