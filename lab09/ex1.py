"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Создание матрицы из списков A и B
"""

# модуль с пользовательскими функциями
from functions import print_matrix

# ввод массивов
a = list(map(int, input("Введите массив A: ").split()))
b = list(map(int, input("Введите массив B: ").split()))

# составление матрицы
matrix = []
for i in range(len(a)):
    tmp = []
    for j in range(len(b)):
        tmp.append(a[i]*b[j])
    matrix.append(tmp)

# вывод полученной матрицы
print("Результат: ")
print_matrix(matrix, j+1, i+1, 8)
