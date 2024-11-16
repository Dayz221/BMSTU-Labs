"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: 
        - Подсчет количества элементов, удовлетворяющих условию
        - Изменение матрицы B (умножение какждого элемента столбца на среднее арифм. этого столбца)
"""

# модуль с пользовательскими функциями
from functions import print_matrix, scan_marix, EPS

# ввод матриц a и b
ac, ar = map(int, input("Введите ширину и высоту матрицы A: ").split())
bc, br = map(int, input("Введите ширину и высоту матрицы B: ").split())

print("Введите матрицу A:")
a = scan_marix(float, ac, ar)

print("Введите матрицу B:")
b = scan_marix(float, bc, br)

# тело программы
for column in range(ac):
    avr_b = 0
    for y in range(br):
        avr_b += b[y][column]
    avr_b /= br

    summ = 0
    for y in range(ar):
        if a[y][column] > avr_b:
            summ += 1

    # вывод промежуточного задания
    print(f"Количество элементов, больших сред. арифм. в {column} столбце A: {summ}")

    if abs(avr_b) > EPS:
        for y in range(br):
            b[y][column] *= avr_b

# вывод измененной матрицы b
print_matrix(b, bc, br, 8)