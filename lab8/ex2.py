"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Смена местами строк с максимальным и минимальным количеством отрицательных элементов
"""

matrix = []  # объект матрицы

# ввод матрицы
columns, rows = map(int, input("Введите количество столбцов и строк матрицы через пробел: ").split())
print(f"Введите {rows} строк матрицы, содержащих {columns} элементов: ")
while len(matrix) < rows:
    enter = [int(el) for el in input().split()]
    if len(enter) != columns:
        print(f"Ширина строки должна быть равна {columns}")
    else:
        matrix.append(enter)

# вывод матрицы
print()
print("Введенная матрица: ")
for row in matrix:
    print(*row, sep='\t')
print()

# анализ матрицы
minimum, maximum = columns+1, 0
minimum_id, maximum_id = 0, 0
for row_id, row in enumerate(matrix):
    cnt = 0
    for el in row:
        if el < 0: cnt += 1
    if cnt > maximum:
        maximum = cnt
        maximum_id = row_id
    if cnt < minimum:
        minimum = cnt
        minimum_id = row_id

# замена строк
matrix[minimum_id], matrix[maximum_id] = matrix[maximum_id], matrix[minimum_id]

# вывод матрицы
print()
print("Результат: ")
for row in matrix:
    print(*row, sep='\t')
print()