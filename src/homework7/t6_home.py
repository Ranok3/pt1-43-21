# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)


def func():
    a = int(input('a = '))
    d = a
    b = 0
    while d > 0:
        b = b * 10 + d % 10
        d = d // 10
    if a == b:
        print('Да, является')
    else:
        print('Не является')


if __name__ == "__main__":
    func()