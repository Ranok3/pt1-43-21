"""
2.	Создайте декоратор, который вызывает задекорированную функцию пока она
не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
"""


class TooManyErrors(Exception):
    pass


def try_repeat(func):
    def wrapper():
        count = func()
        while count > -1:
            try:
                if count == 0:
                    raise TooManyErrors
            except TooManyErrors:
                print('Слишком много ошибок')
                break
            else:
                a = input('a = ')
                b = input('b = ')
                try:
                    return print(int(a) + int(b))
                except ValueError:
                    print('Неверный ввод')
                    count -= 1
    return wrapper


@try_repeat
def exception_func():
    return 3


exception_func()
