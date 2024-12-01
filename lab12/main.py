'''
    Выполнил: Пэкэлэу Даниил
    Группа: ИУ7-16Б
    Назначение: 
        - текстовый процессор
        - п. 6 - Вычитание и умножение
        - п. 7 - Наиболее часто встречающееся слово в каждом предложении
'''

from functions import *

menu = """
Действия с текстом:
0) Выйти
1) Выровнять текст по левому краю
2) Выровнять текст по правому краю
3) Выровнять текст по ширине
4) Удаление всех вхождений заданного слова
5) Замена одного слова другим во всём тексте
6) Вычисление арифметических выражений над целыми числами внутри текста
7) Найти и затем удалить слово или предложение по варианту
"""

text = [
    'Есть тети как тети',
    'Есть дяди как дяди',
    'Есть люди как люди',
    'Есть ИУ7-14Б как ИУ7-14Б',
    'Но в жизни бывает',
    'Порой по-другому',
    'Есть дяди как тети',
    'Есть тети как дяди',
    'Есть ИУ7-14Б как люди',
    'И люди как ИУ7-14Б',
    'ac 80 - 2 * 10 - 99 abc 99 - 5 a 5 * 5'
]

# Тело программы
isRunning = True
currentAlignment = alignLeft
while isRunning:
    print(*text, sep='\n')
    print(menu)
    
    enter = input("Введите номер действия с текстом: ")

    match enter:
        case "0":
            isRunning = False

        case "1":
            text = alignLeft(text)
            currentAlignment = alignLeft
        case "2":
            text = alignRight(text)
            currentAlignment = alignRight
        case "3":
            text = stretch(text)
            currentAlignment = stretch

        case "4":
            word = input("Введите слово, которое хотите удалить: ")
            text = deleteWord(text, word, currentAlignment)

        case "5":
            word1 = input("Введите слово, которое хотите заменить: ")
            word2 = input("Введите слово, которым хотите заменить: ")
            text = replaceWord(text, word1, word2, currentAlignment)

        case "6":
            text = countExpressions(text, currentAlignment)

        case "7":
            text, word = findAndDelete(text, currentAlignment)
            print("Самое частоповторяющееся слово:", word)
            pause()

        case _:
            print("Введено некорректное число!")
            pause()
    
    clear()
