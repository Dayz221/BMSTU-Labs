"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение:
        - вычисление приближенного интеграла функции методами левых прямоугольников и трапеции
        - нахождение относительной и абсолютной погрешностей для каждого метода
        - нахождение количества разбиений для функции с меньшей точностью
"""

# импорт пользовательских функций
from functions import *
import math

# функции
def f(x):
    return 1/x

def af(x):
    return math.log(abs(x))

# ввод данных
a, b, n1, n2, eps = 0, 0, 0, 0, 0
isCorrect = False
while not isCorrect:
    try:
        a, b = map(float, input("Введите начало и конец интегрирования: ").split())
        if a >= b: print("Точка старта должна быть меньше точки конца")
        else: isCorrect = True
    except:
        print("Введены некорректные данные")

isCorrect = False
while not isCorrect:
    try:
        n1, n2 = map(int, input("Введите количество отрезков разбиения: ").split())
        if n1 < 2 or n2 < 2: print("Количество разбиений должно быть больше 2")
        else: isCorrect = True
    except:
        print("Введены некорректные данные")

isCorrect = False
while not isCorrect:
    try:
        eps = float(input("Введите eps: "))
        if eps <= 0: print("Число eps должно быть больше 0")
        else: isCorrect = True
    except:
        print("Введены некорректные данные")
    

# вычисление приближенных интегралов
isCorrect = False
try:
    i1, i2 = leftRectsInt(f, a, b, n1), leftRectsInt(f, a, b, n2)
    i3, i4 = trapInt(f, a, b, n1), trapInt(f, a, b, n2)
    trueValue = af(b) - af(a)
    isCorrect = True
except:
    print("Невозможно посчитать интеграл при данных параметрах")

if isCorrect:
    # вычисление погрешностей
    rel1, rel2 = abs(trueValue-i1), abs(trueValue-i2)
    rel3, rel4 = abs(trueValue-i3), abs(trueValue-i4)

    # вывод таблицы
    table = [
        ["", "N1", "Абс. / Отн. погрешность", "N2", "Абс. / Отн. погрешность"],
        ["Метод левых прямоугольников", 
        f"{i1:3.6g}", 
        f"{rel1:3.6g} / {rel1*100/trueValue:3.6g}%", 
        f"{i2:3.6g}", 
        f"{rel2:3.6g} / {rel2*100/trueValue:3.6g}%"
        ],
        ["Метод трапеции", 
        f"{i3:3.6g}", 
        f"{rel3:3.6g} / {rel3*100/trueValue:3.6g}%", 
        f"{i4:3.6g}", 
        f"{rel4:3.6g} / {rel4*100/trueValue:3.6g}%"
        ],
    ]
    printTable(table)

    print(f"Истинное значение интеграла: {trueValue}")

    # Нахождение количества разбиений
    if min(rel1, rel2) < min(rel3, rel4):
        print("Метод левых прямоугольников оказался более точным") # невозможно =)
        
        cnt = findSamplesCountEffective(trapInt, f, a, b, eps)
        if (cnt == MAX_CNT): print("Не удалось достичь необходимой точности")
        else: print(f"Количество разбиений для достижения точности eps: {cnt}")
        
        val = trapInt(f, a, b, cnt)
        print(f"Приближенное значение интеграла: {val}")

    else:
        print("Метод трапеции оказался более точным")
        
        cnt = findSamplesCountEffective(leftRectsInt, f, a, b, eps)    
        if (cnt == MAX_CNT): print("Не удалось достичь необходимой точности")
        else: print(f"Количество разбиений для достижения точности eps: {cnt}")

        val = leftRectsInt(f, a, b, cnt)
        print(f"Приближенное значение интеграла: {val}")