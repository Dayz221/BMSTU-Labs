'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Описание: вычисление суммы бесконечного ряда
'''

# ==== ВВОД ДАННЫХ ====

x = float(input("Введите число x: "))
eps = float(input("Введите число eps: "))
step_size = int(input("Введите шаг вывода: "))
iters = int(input("Введите количество итераций: "))

# ==== ТЕЛО ПРОГРАММЫ ====

# вывод шапки таблицы вывода
print("----------------------------------")
print("| № итерации |    t    |    s    |")
print("----------------------------------")

summ = 0  # переменная для хранения суммы ряда
for n in range(iters):
    cur = (-1/2)**n  # вычисление значения текущего элемента
    if abs(cur) < eps:  # проверка текущей точности
        break
    else:
        summ += cur
    
    if n % step_size == 0:
        print(f"| {n:10} | {cur:7g} | {summ:7g} |")

print("----------------------------------")