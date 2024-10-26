"""
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: определение принадлежности точки с координатами (x, y) фигуре
    Вариант: 3
"""

# ====== ОБЪЯВЛЕНИЕ ФУНКЦИЙ ======

# функция, задающая фигуру
def isConatin(x, y):
    return ((-3 <= x < 0) and (y <= (9-x**2)**0.5+3) and (y >= x**2-6) and (y >= x)) or \
           ((0 <= x <= 3) and (y <= (9-x**2)**0.5+3) and (y >= x**2-6) and (y >= -x))

# ====== ВВОД ДАННЫХ ======

x = float(input("Введите координату x: "))
y = float(input("Введите координату Y: "))

# ====== ПОДСЧЕТЫ ======

_isContain = isConatin(x, y)

# ====== ВЫВОД РЕЗУЛЬТАТОВ ======

print(f"Точна с координатами ({x:.3g} ; {y:.3g}) " + ("принадлежит фигуре" if _isContain else "не принадлежит фигуре") )