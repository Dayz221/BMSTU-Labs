from functions import *

# функции
def f(x):
    return x**3 + x - 1

def af(x):
    return x**4/4 + x**2/2 - x

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
i1, i2 = leftRectsInt(f, a, b, n1), leftRectsInt(f, a, b, n2)
i3, i4 = trapInt(f, a, b, n1), trapInt(f, a, b, n2)
trueValue = af(b) - af(a)

# вычисление погрешностей
rel1, rel2 = abs(trueValue-i1), abs(trueValue-i2)
rel3, rel4 = abs(trueValue-i3), abs(trueValue-i4)

# вывод таблицы
table = [
    ["", "N1", "Абс. / Отн.", "N2", "Абс. / Отн."],
    ["Метод левых прямоугольников", 
     f"{i1:3g}", 
     f"{rel1:3g} / {rel1*100/trueValue:3g}%", 
     f"{i2:3g}", 
     f"{rel2:3g} / {rel2*100/trueValue:3g}%"
    ],
    ["Метод трапеции", 
     f"{i3:3g}", 
     f"{rel3:3g} / {rel3*100/trueValue:3g}%", 
     f"{i4:3g}", 
     f"{rel4:3g} / {rel4*100/trueValue:3g}%"
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