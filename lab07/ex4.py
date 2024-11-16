'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: удаление четных элементов из массива
'''

n = int(input("Введите количество элементов: "))  # Ввод количества слов
alphabet = "bcdfghjklmnpqrstvwxz"  # Веременная, хранящая буквы для замены

# Ввод массива
arr = []
for el in range(n):
    enter = input()
    arr.append(enter)

# Тело программы
for i in range(len(arr)):
    for letter in alphabet:
        arr[i] = arr[i].replace(letter, letter.upper())

# Вывод измененного массива
print("\nРезультат работы:", *arr, sep="\n")