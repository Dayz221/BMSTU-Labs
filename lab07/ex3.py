'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: удаление четных элементов из массива
'''

n = int(input("Введите длину массива: "))  # Ввод количества слов
print("Введите массив строк:")

# Ввод массива
arr = []
for _ in range(n):
    enter = input()
    arr.append(enter)

# Тело программы
max_len = 0
str_with_max_len = ""

for el in arr:
    cnt = 0
    max_cnt = 0
    for letter in el:
        if letter == ' ':
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0

    if max_cnt > max_len:
        max_len = max_cnt
        str_with_max_len = el

# Вывод результата работы
if max_len != 0:
    print("Элемент с максимальным количеством подряд идущих пробелов: \"" + str_with_max_len + "\"")
else:
    print("Не найден элемент с пробелами")