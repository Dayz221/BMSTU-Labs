"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Поворот матрицы по часовой и против часовой стрелки
"""

# модуль с пользовательскими функциями
from functions import scan_marix, print_matrix

# функции поворота матрицы
def rotateLeft(matrix):
    for layer in range(n//2):
        for x in range(n-2*layer-1):
            t = matrix[layer][x+layer]
            matrix[layer][x+layer] = matrix[x+layer][n-layer-1]
            matrix[x+layer][n-layer-1] = matrix[n-layer-1][n-x-layer-1]
            matrix[n-layer-1][n-x-layer-1] = matrix[n-layer-x-1][layer]
            matrix[n-layer-x-1][layer] = t

def rotateRight(matrix):
    for layer in range(n//2):
        for x in range(n-2*layer-1):
            t = matrix[layer][x+layer]
            matrix[layer][x+layer] = matrix[n-layer-x-1][layer]
            matrix[n-layer-x-1][layer] = matrix[n-layer-1][n-x-layer-1]
            matrix[n-layer-1][n-x-layer-1] = matrix[x+layer][n-layer-1]
            matrix[x+layer][n-layer-1] = t

# ввод матрицы
n = int(input("Введите размер квадратной матрицы: "))
matrix = scan_marix(int, n, n)

# поворот по часовой стрелке и вывод матрицы
rotateRight(matrix)
print("Результат поворота по часовой стрелке: ")
print_matrix(matrix, n, n, 8)

# поворот против часовой стрелки и вывод матрицы
rotateLeft(matrix)
print("Результат поворота против часовой стрелки: ")
print_matrix(matrix, n, n, 8)