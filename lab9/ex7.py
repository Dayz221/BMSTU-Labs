"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: вывод среза 3-х мерной матрицы хитровыебаным способом
"""

# модуль с пользовательскими функциями
from functions import scan_marix

# ввод матрицы
sx, sy, sz = map(int, input("Введите размер матрицы (x y z): ").split())
matrix = []
print("Введите матрицу:")
for _ in range(sz):
    matrix.append(scan_marix(str, sx, sy))

# тело программы
if sx >= sy and sx >= sz:
    c = sx//2
    for y in range(sy):
        for z in range(sz):
            print(f"{matrix[z][y][c]:>8}", end=' ')
        print()

elif sy >= sx and sy >= sz:
    c = sy//2
    for z in range(sz):
        for x in range(sx):
            print(f"{matrix[z][c][x]:>8}", end=' ')
        print()
else:
    c = sz//2
    for y in range(sy):
        for x in range(sx):
            print(f"{matrix[c][y][x]:>8}", end=' ')
        print()