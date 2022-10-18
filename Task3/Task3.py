# Задайте список из n чисел последовательности: 1 + (1/n)^n и выведите на экран их сумму.

n = int(input('Enter the number n: '))
res = 0
lst = list(range(1, n + 1))
print (lst)
for i in lst:
    res += (1 + (i)**(-i))
print (f'Сумма последовательности {n} чисел = {res}')
