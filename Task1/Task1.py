# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != '.' and i != ',':
            sum += int(i)
    return sum


num = input('Введите вещественное число: ')

print(f'Сумма цифр числа = {sumNums(num)}')
