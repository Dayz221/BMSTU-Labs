"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: 
        - Нахождение масимального элемента над главной диагональю
        - Нахождение минимального элемента под побочной диагональю
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

# анализ матрицы
maximum, minimum = matrix[0][n-1], matrix[n-1][n-1]
for y in range(n):
    for x in range(y+1, n):
        maximum = max(maximum, matrix[y][x])

for y in range(n):
    for x in range(n-y, n):
        minimum = min(minimum, matrix[y][x])

# результат
print("Максимальное значение над главной диагональю: ", maximum)
print("Минимальное значение под побочной диагональю: ", minimum)
