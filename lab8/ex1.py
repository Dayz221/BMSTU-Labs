"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: Вывод строки с максимальным количеством идущих подряд одинаковых элементов
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
maximum, maximum_id = 0, 0
for row_id, row in enumerate(matrix):
    cur, cur_max = 1, 0
    for i in range(len(row)):
        if i != 0 and row[i] == row[i-1]:
            cur += 1
        else:
            cur = 1
        cur_max = max(cur_max, cur)
    if cur_max > maximum:
        maximum = cur_max
        maximum_id = row_id

# вывод результата
if maximum == 1:
    print("В матрице нет подряд идущих одинаковых элементов")
else:
    print("Строка с максимальным количеством идущих подряд одинаковых элементов: ", maximum_id+1)
    print("Максимальное количество идущих подряд одинаковых элементов: ", maximum)
