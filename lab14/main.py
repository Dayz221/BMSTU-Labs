from functions import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
curFile = ""

menu = """Выберите действие:
    1. Выбрать файл для работы
    2. Инициализировать базу данных
    3. Вывести содержимое базы данных
    4. Добавить запись в произвольное место базы данных
    5. Удалить произвольную запись из базы данных
    6. Поиск по одному полю
    7. Поиск по двум полям
"""

while True:
    clear()
    printLog(f"Текущий файл: {curFile if curFile else 'файл не выбран'}\n")
    print(menu)

    match input("Введите номер действия: "):
        case "1":
            curFile = changeFile(BASE_DIR)

        case "2":
            if curFile:
                initFile(curFile)
            else:
                if input(Fore.YELLOW + "Файл не выбран. Желаете создать новый? (y/N): " + Fore.WHITE).lower() == 'y':
                    name = ""
                    while len(name) == 0:
                        name = input("Введите название файла: ")
                    curFile = os.path.join(BASE_DIR, name)
                    open(curFile, 'w+').close()
                    initFile(curFile)

        case "3":
            if curFile:
                clear()
                print(Fore.WHITE + "База данных: " + Fore.CYAN + curFile + Fore.WHITE)
                printTable(curFile)
                pause()
            else:
                printErr("Файл не выбран!")
                pause()

        case "4":
            if curFile:
                clear()
                printLog("Добавить новую запись:")
                printTable(curFile)
                print()
                line = -1
                while True:
                    try: 
                        enter = input(Fore.GREEN + "Введите номер строки, куда хотите вставить новую запись (изначально в конец): " + Fore.WHITE)
                        if enter == "":
                            break
                        line = int(enter)
                        break
                    except:
                        printErr("Введено неверное значение!")
                
                print()
                addEntry(curFile, line)
            else:
                printErr("Файл не выбран!")
                pause()

        case "5":
            if curFile:
                clear()
                printLog("Удалить запись:")
                printTable(curFile)
                print()

                cnt = getEntriesCount(curFile)
                line = -1
                while True:
                    try: 
                        enter = input(Fore.GREEN + "Введите номер строки, которую хотите удалить: " + Fore.WHITE)
                        line = int(enter)
                        if line >= cnt:
                            printErr("Введено неверное значение!")
                            continue
                        break
                    except:
                        printErr("Введено неверное значение!")
                
                deleteEntry(curFile, line)
            else:
                printErr("Файл не выбран!")
                pause()

        case "6":
            if curFile:
                clear()
                printLog("Найти запись:")
                printTable(curFile)
                print()

                fieldName = ""
                fieldValue = None

                while not fieldName:
                    fieldName = input(Fore.GREEN + f"Введите название поля ({', '.join([el for el in MODEL.keys()])}): " + Fore.WHITE)
                    if fieldName not in MODEL.keys():
                        printErr("Неверное название поля!")
                        fieldName = ""

                while True:
                    value = input(Fore.GREEN + f"Введите значение поля: " + Fore.WHITE)
                    success, fieldValue = MODEL[fieldName]['validator'](value)
                    if not success:
                        printErr("Неверное значение поля!")
                    else:
                        break
                
                clear()
                printLog("Найденные поля:")
                findEntry(curFile, **{fieldName: fieldValue})
                pause()
            else:
                printErr("Файл не выбран!")
                pause()

        case "7":
            if curFile:
                clear()
                printLog("Найти запись:")
                printTable(curFile)
                print()

                fieldName1 = ""
                fieldName2 = ""
                fieldValue1 = None
                fieldValue2 = None

                while not fieldName1:
                    fieldName1 = input(Fore.GREEN + f"Введите название поля 1 ({', '.join([el for el in MODEL.keys()])}): " + Fore.WHITE)
                    if fieldName1 not in MODEL.keys():
                        printErr("Неверное название поля!")
                        fieldName1 = ""

                while True:
                    value = input(Fore.GREEN + f"Введите значение поля 1: " + Fore.WHITE)
                    success, fieldValue1 = MODEL[fieldName1]['validator'](value)
                    if not success:
                        printErr("Неверное значение поля!")
                    else:
                        break

                while not fieldName2:
                    fieldName2 = input(Fore.GREEN + f"Введите название поля 2 ({', '.join([el for el in MODEL.keys()])}): " + Fore.WHITE)
                    if fieldName2 not in MODEL.keys():
                        printErr("Неверное название поля!")
                        fieldName2 = ""

                while True:
                    value = input(Fore.GREEN + f"Введите значение поля 2: " + Fore.WHITE)
                    success, fieldValue2 = MODEL[fieldName1]['validator'](value)
                    if not success:
                        printErr("Неверное значение поля!")
                    else:
                        break
                
                clear()
                printLog("Найденные поля:")
                findEntry(curFile, **{fieldName1: fieldValue1, fieldName2: fieldValue2})
                pause()
            else:
                printErr("Файл не выбран!")
                pause()

        case _:
            printErr("Введите корректный номер действия!")
            pause()   
