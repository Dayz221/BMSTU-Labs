"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Вывод столбца с масимальным количеством 0 элементов
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
maximum, maximum_id = 0, -1
for x in range(columns):
    cur = 0
    for y in range(rows):
        el = matrix[y][x]
        if el == 0:
            cur += 1
    if cur > maximum:
        maximum = cur
        maximum_id = x

# вывод результата
if maximum_id == -1:
    print("В матрице нет столбцов с 0 элементами")
else:
    print("Стоблец с максимальным количеством 0 элементов: ", maximum_id+1)
    print("Максимальное количество 0 элементов: ", maximum)
