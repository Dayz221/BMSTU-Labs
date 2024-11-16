"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: 
        - замена всех строчных согласных букв на заглавные
        - замена всех заглавных гласных букв на строчные
"""

# модуль с пользовательскими функциями
from functions import print_matrix, scan_marix

# ввод матриц
m, n = map(int, input("Введите размер матрицы A: ").split())

print("Введите матрицу:")
matrix = scan_marix(str, m, n)

# тело программы
for y in range(n):
    for x in range(m):
        if matrix[y][x].lower() in 'aeyuio':
            matrix[y][x] = matrix[y][x].lower()
        else:
            matrix[y][x] = matrix[y][x].upper()

# вывод результата
print("Результат")
print_matrix(matrix, m, n, 1) 