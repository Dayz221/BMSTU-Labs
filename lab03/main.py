'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Задачи программы:
        - вычисление длин сторон треугольника
        - вычисление длины биссектрисы, проведенной из наибольшего угла
        - определение, является ли треугольник тупоугольным
        - определение, находится ли точка внутри треугольника
        - вычисление расстояния от точки до близжайшей стороны треугольника
'''

# ====== ВВОД ДАННЫХ 3 ТОЧЕК ======

x1, y1 = map(float, input("Введите координаты 1 точки в формате: X Y\n").split())
x2, y2 = map(float, input("Введите координаты 2 точки в формате: X Y\n").split())
x3, y3 = map(float, input("Введите координаты 3 точки в формате: X Y\n").split())

# ====== НЕОБХОДИМЫЕ ВЫЧИСЛЕНИЯ ======

# вычисление длин сторон
len1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
len2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
len3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

# проверка того, что треугольник существует
if not (len1 < len2 + len3 and len2 < len1 + len3 and len3 < len1 + len2):
    print("Треугольника с заданными координатами не существует")
    exit()

maxLen = max(len1, len2, len3)
a, b, c = 0, 0, maxLen

if maxLen == len1:
    a, b = len2, len3
elif maxLen == len2:
    a, b = len1, len3
else:
    a, b = len1, len2

bissLen = (a*b*(a+b+c)*(a+b-c))**0.5/(a+b)

if c**2 > a**2 + b**2:
    print("Треугольник является тупоугольным")
else:
    print("Треугольник не является тупоугольным")

print(f"Длина стороны AB: {len1:5f}\nДлина стороны BC: {len2:5f}\nДлина стороны AC: {len3:5f}\nДлина биссектрисы: {bissLen:5f}")

# ввод координат точки
x0, y0 = map(float, input("Введите координаты точки в формате: X Y\n").split())

# проверка того, что точка внутри треуголька
n = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
p = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
k = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
 
if (n >= 0 and p >= 0 and k >= 0) or (n <= 0 and p <= 0 and k <= 0):
    print("Заданная точка находится внутри треугольника")

    l1 = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)/(((y2-y1)**2 + (x2-x1)**2)**0.5)
    l2 = abs((y3-y2)*x0 - (x3-x2)*y0 + x3*y2 - y3*x2)/(((y3-y2)**2 + (x3-x2)**2)**0.5)
    l3 = abs((y1-y3)*x0 - (x1-x3)*y0 + x1*y3 - y1*x3)/(((y1-y3)**2 + (x1-x3)**2)**0.5)

    print(f"Минимальное расстояние до прямой: {min(l1, l2, l3):5f}")

else:
    print("Заданная точка находится снаружи треугольника")