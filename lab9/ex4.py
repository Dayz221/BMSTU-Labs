"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: 
        - Поиск максимальных элементов по строкам из массива
        - Создание массива R с полученными элементами
        - Вычисление среднего арифмитического из элементов R
"""

# модуль с пользовательскими функциями
from functions import print_matrix, scan_marix

# ввод матрицы
m, n = map(int, input("Введите размер матрицы D: ").split())

print("Введите матрицу D:")
matrix = scan_marix(float, m, n)

# ввод массива l
arr = list(map(int, input("Введите массив L: ").split()))

# массив r и среднее арифмитическое
r = []
avg = 0

# тело программы
for row in arr:
    if not (0 <= row < n):
        print(f"Строки №{row} нет в матрице...")
        continue

    maximum = matrix[row][0]
    for el in matrix[row]:
        if el > maximum:
            maximum = el
    r.append(maximum)
    avg += maximum

avg /= len(arr)

# вывод результатов
print("Матрица D:")
print_matrix(matrix, m, n, 8)
print(f"Массив l: {' '.join(map(str, arr))}")
print(f"Массив r: {' '.join(map(str, r))}")
print(f"Среднее арифмитическое массива r: {avg}")