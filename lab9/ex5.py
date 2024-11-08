"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: 
        - произведение 2 матриц
"""

# модуль с пользовательскими функциями
from functions import print_matrix, scan_marix

def dot(matrix1, matrix2):
    matrix = []
    rows = len(matrix2)
    for y in range(rows):
        tmp = []
        for x in range(len(matrix2[0])):
            el = 0
            for i in range(len(matrix2)):
                el += matrix2[i][x] * matrix1[y][i]
            tmp.append(el)
        matrix.append(tmp)
    return matrix

# ввод матриц
am, an = map(int, input("Введите размер матрицы A: ").split())
bm = int(input("Введите количество столбцов матрицы B: "))

print("Введите матрицу A:")
a = scan_marix(float, am, an)

print("Введите матрицу B:")
b = scan_marix(float, bm, am)

# тело программы
matrix = dot(a, b)

# вывод результатов:
print("Полученная матрица")
print_matrix(matrix, bm, am, 8)