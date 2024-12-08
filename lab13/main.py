from functions import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
curFile = ""

menu = """Выберите действие:
    1. Выбрать файл для работы
    2. Инициализировать базу данных
    3. Вывести содержимое базы данных
    4. Добавить запись в конец базы данных
    5. Поиск по одному полю
    6. Поиск по двум полям
"""

while True:
    clear()
    printLog(f"Текущий файл: {curFile if curFile else 'файл не выбран'}\n")
    printText(menu)

    match input("Введите номер действия: "):
        case "1":
            curFile = changeFile(BASE_DIR)

        case "2":
            if not curFile:
                if (
                    input(
                        Fore.YELLOW
                        + "Файл не выбран! Желаете создать новый файл? (y/N): "
                    ).lower()
                    == "y"
                ):
                    fileName = input(Fore.WHITE + "Введите название файла: ")
                    curFile = os.path.join(BASE_DIR, fileName)
                    initDataBase(curFile)
            else:
                initDataBase(curFile)

        case "3":
            if not curFile:
                printErr("Сначала необходимо выбрать файл для работы!")
            else:
                printDataBase(curFile)
            pause()

        case "4":
            if not curFile:
                printErr("Сначала необходимо выбрать файл для работы!")
                pause()
            else:
                addDocument(curFile)

        case "5":
            if not curFile:
                printErr("Сначала необходимо выбрать файл для работы!")
            else:
                field = input(Fore.GREEN + f"Введите поле ({', '.join([key for key in DB_MODEL.keys()])}): " + Fore.WHITE)
                if field not in DB_MODEL.keys():
                    printErr("Такого поля нет!")
                    pause()
                    continue
                
                success, value = convert(DB_MODEL[field]['type'], input(Fore.GREEN + "Введите значение поля: " + Fore.WHITE))
                if not success:
                    printErr("Введено некорректное значение!")
                    pause()
                    continue

                findElement(curFile, **{field:value})
            pause()

        case "6":
            if not curFile:
                printErr("Сначала необходимо выбрать файл для работы!")
            else:
                field1 = input(Fore.GREEN + f"Введите поле 1 ({', '.join([key for key in DB_MODEL.keys()])}): " + Fore.WHITE)
                if field1 not in DB_MODEL.keys():
                    printErr("Такого поля нет!")
                    pause()
                    continue
                success, value1 = convert(DB_MODEL[field1]['type'], input(Fore.GREEN + "Введите значение поля 1: " + Fore.WHITE))
                if not success:
                    printErr("Введено некорректное значение!")
                    pause()
                    continue

                field2 = input(Fore.GREEN + f"Введите поле 2 ({', '.join([key for key in DB_MODEL.keys()])}): " + Fore.WHITE)
                if field2 not in DB_MODEL.keys():
                    printErr("Такого поля нет!")
                    pause()
                    continue
                success, value2 = convert(DB_MODEL[field2]['type'], input(Fore.GREEN + "Введите значение поля 2: " + Fore.WHITE))
                if not success:
                    printErr("Введено некорректное значение!")
                    pause()
                    continue

                findElement(curFile, **{field1:value1, field2:value2})
            pause()

        case _:
            printErr("Введите корректный номер действия!")
            pause()   
