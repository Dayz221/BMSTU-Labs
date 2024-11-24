'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение:
        - сортировка списка
        - вывод результатов тестирования алгоритма сортировки
    Метод сортировки: пирамидальная сортировка
'''

from functions import *
from random import randint

lst = [int(el) for el in input("Введите массив: ").split()]
(lst, operations), sortTime = getWithTime(heapSort)(lst[:])

print(f"Результат сортировки:", *lst)
print('Посчитано за:', sortTime, 'c. и', operations, 'перестановок')

n1, n2, n3 = map(int, input("Введите n1, n2 и n3 через пробел: ").split())

lst11 = [el for el in range(n1)]
lst12 = [el for el in range(n2)]
lst13 = [el for el in range(n3)]

lst21 = [randint(0, n1) for _ in range(n1)]
lst22 = [randint(0, n2) for _ in range(n2)]
lst23 = [randint(0, n3) for _ in range(n3)]

lst31 = [n1-1-el for el in range(n1)]
lst32 = [n1-1-el for el in range(n2)]
lst33 = [n1-1-el for el in range(n3)]

(_, k1), t1 = getWithTime(heapSort)(lst11)
(_, k2), t2 = getWithTime(heapSort)(lst21)
(_, k3), t3 = getWithTime(heapSort)(lst31)

(_, k4), t4 = getWithTime(heapSort)(lst12)
(_, k5), t5 = getWithTime(heapSort)(lst22)
(_, k6), t6 = getWithTime(heapSort)(lst32)

(_, k7), t7 = getWithTime(heapSort)(lst13)
(_, k8), t8 = getWithTime(heapSort)(lst23)
(_, k9), t9 = getWithTime(heapSort)(lst33)

table = [
    ['', 'N1', 'N2', 'N3'],
    ['', 'Время / перестановки', 'Время / перестановки', 'Время / перестановки'],
    ['Упорядоченный список', f"{t1:.5g} с. / {k1:.5g}", f"{t2:.5g} с. / {k2:.5g}", f"{t3:.5g} с. / {k3:.5g}"],
    ['Случайный список', f"{t4:.5g} с. / {k4:.5g}", f"{t5:.5g} с. / {k5:.5g}", f"{t6:.5g} с. / {k6:.5g}"],
    [' Упорядоченный в обратном порядке', f"{t7:.5g} с. / {k7:.5g}", f"{t8:.5g} с. / {k8:.5g}", f"{t9:.5g} с. / {k9:.5g}"]
]

printTable(table)