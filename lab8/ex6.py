"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Выполняет транспонирование матрицы
"""

matrix = []  # объект матрицы

# ввод матрицы
n = int(input("Введите размер квадратной матрицы: "))
print(f"Введите матрицу {n}x{n}: ")
while len(matrix) < n:
    enter = [int(el) for el in input().split()]
    if len(enter) != n:
        print(f"Ширина строки должна быть равна {n}")
    else:
        matrix.append(enter)

# вывод матрицы
print()
print("Введенная матрица: ")
for row in matrix:
    print(*row, sep='\t')
print()

# транспонирование матрицы
for y in range(n):
    for x in range(y):
        matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

# результат
print()
print("Результат: ")
for row in matrix:
    print(*row, sep='\t')
print()