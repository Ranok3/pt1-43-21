"""
3.	Tuple practice
1.	Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""

cort = ([1, 2, 3], )
print(len(cort))
for i in cort:
    print(i)
