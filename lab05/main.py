'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение:
        - Вывод таблицы для построения графиков функций по точкам
        - Построение графика функции
'''

# подключение модуля math
from math import exp, log

GRAPH_WIDTH = 80  # константа ширины графика, объявленная в соответствии с pep8

# ==== ВВОД И ПРОВЕРКА ДАННЫХ ==== #

start, end, step = map(float, input("Введите точки старта, конца и шаг через пробел: ").split())

if start <= 0:
    print("Точка старта должна быть больше 0")
    exit()

if start >= end:
    print("Точка старта должна быть меньше точки конца")
    exit()

if step <= 0:
    print("Шаг функции должен быть больше нуля")
    exit()

# ==== ВЫВОД ТАБЛИЦЫ ЗНАЧЕНИЙ ==== #

# вывод шапки таблицы
print("----------------------------------------------------")
print("|     x     |     y1     |     y2     |     y3     |")
print("----------------------------------------------------")

x = start
ymin, ymax = 10**9, -(10**9)  # переменные для хранения минимального и максимального y
positiveCount = 0  # счетчик точек с положительными значениями
while x < end + step:
    s1 = 2 * log(x) - 1 / x  # по данной функции чертится график
    s2 = x**3 - 7 * x + 6.5
    s3 = exp(-abs(s1 + s2))

    positiveCount += s1 > 0
    ymin = s1 if s1 < ymin else ymin
    ymax = s1 if s1 > ymax else ymax

    print(f"| {x:^9.5g} | {s1:^10.5g} | {s2:^10.5g} | {s3:^10.5g} |")  # вывод данных в таблицу

    x += step

print("----------------------------------------------------")  # конец таблицы
print(f"Количество положительных значений s1: {positiveCount}\n\n")

# ввод количества засечек на оси Oy
cnt = int(input("Введите количество засечек (4-8): "))

# проверка введенного значения
if not (4 <= cnt <= 8):
    print("Введите корректное количество засечек (4-8)")
    exit()

x = start
zero_y = round(-ymin * GRAPH_WIDTH / (ymax - ymin))  # нахождение относительной координаты нуля

# вывод засечек
print(" " * 6, end="")
for i in range(cnt):
    print(f"{ymin+(ymax-ymin)*i/(cnt-1):^5f}{' '*(GRAPH_WIDTH//(cnt-1)-5)}", end="")
print()

print("-" * (15 + GRAPH_WIDTH) + "> y") # вывод оси Oy
while x < end + step:
    y = 2 * log(x) - 1 / x
    graph_y = round((y - ymin) * GRAPH_WIDTH / (ymax - ymin))  # нахождение относительной координаты y

    # построение графика
    if zero_y == graph_y:
        print(f"{x:<7.4g} |{' ' * graph_y}*{' ' * (GRAPH_WIDTH-graph_y)}")
    elif zero_y > graph_y:
        print(
            f"{x:<7.4g} |{' ' * graph_y}*{' ' * (zero_y-graph_y-1)}|{' ' * (GRAPH_WIDTH-zero_y)}"
        )
    else:
        print(
            f"{x:<7.4g} |{' ' * zero_y}|{' ' * (graph_y - zero_y - 1)}*{' ' * (GRAPH_WIDTH-graph_y)}"
        )

    x += step
