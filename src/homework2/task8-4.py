# У вас есть число и нужно определить какая цифра из этого числа
# является наибольшей.
#
# Входные данные: Положительное целое число.
#
# Выходные данные: Целое число (0-9).

a = int(input('a = '))
b = 0
while a > 0:
    if a % 10 > b:
        b = a % 10
    a = a // 10
print(b)

