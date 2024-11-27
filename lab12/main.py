'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: текстовый процессор
'''

from os import path, system
from functions import alignLeft, alignRight, stretch, deleteWord

menu = """
Действия с текстом:
0) Выйти и сохранить текст
1) Выровнять текст по левому краю
2) Выровнять текст по правому краю
3) Выровнять текст по ширине
4) Удаление всех вхождений заданного слова
5) Замена одного слова другим во всём тексте
6) Вычисление арифметических выражений над целыми числами внутри текста
7) Найти и затем удалить слово или предложение по варианту
"""

def update():
    system("cls")

def pause():
    print("Нажмите любую клавишу...")
    system("pause > nul")

# Ввод имени файла (файл должен лежать в папке с проектом)
correct = False
filePath = ""
while not correct:
    fileName = input("Введите название файла: ")
    filePath = path.join(path.dirname(__file__), fileName)
    if not (path.exists(filePath) and fileName.strip() != ""):
        print("Такого файла в папке с проектом нет...")
    else:
        correct = True

# Чтение файла
text = []
with open(filePath, 'r', encoding='UTF-8') as file:
    text = [line.strip('\n') for line in file.readlines()]
system("cls")

# Тело программы
isRunning = True
while isRunning:
    print(*text, sep='\n')
    print(menu)
    
    enter = input("Введите номер действия с текстом: ")

    match enter:
        case "0":
            with open(filePath, 'w', encoding='UTF-8') as file:
                file.write('\n'.join(text))
            isRunning = False

        case "1":
            text = alignLeft(text)
        case "2":
            text = alignRight(text)
        case "3":
            text = stretch(text)
        case "4":
            word = input("Введите слово, которое хотите удалить: ")
            text = deleteWord(text, word, stretch)
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case _:
            print("Введено некорректное число!")
            pause()
    
    update()
