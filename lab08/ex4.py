"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Смена местами столбцов с минимальной и максимальной суммами
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
maximum, maximum_id = sum([matrix[y][0] for y in range(rows)]), 0
minimum, minimum_id = maximum, 0
for x in range(1, columns):
    cur_summ = sum([matrix[y][x] for y in range(rows)])
    if cur_summ > maximum:
        maximum = cur_summ
        maximum_id = x
    if cur_summ < minimum:
        minimum = cur_summ
        minimum_id = x

# замена столбцов
for y in range(rows):
    matrix[y][minimum_id], matrix[y][maximum_id] = matrix[y][maximum_id], matrix[y][minimum_id]

# вывод матрицы
print()
print("Результат: ")
for row in matrix:
    print(*row, sep='\t')
print()