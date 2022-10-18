# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Факториал.
num = int(input('Enter the number: '))
factorial = 1
if num >= 0:
    for i in range(1, num + 1):
        factorial = i * factorial
        print(f'{i}!= {factorial}')
else:
    print('Невозможно вычислить факториал отрицательного числа')
