import os
from colorama import Fore
from dbModel import MODEL, STRUCT, decodeEntry
import time


def changeFile(dir: str) -> str:
    while True:
        clear()
        folders: list[str] = []
        files: list[str] = []

        print("Текущая директория: " + Fore.CYAN + dir + "\n" + Fore.WHITE)

        for entry in os.listdir(dir):
            if os.path.isdir(os.path.join(dir, entry)):
                folders.append(entry)
            elif os.path.isfile(os.path.join(dir, entry)):
                files.append(entry)

        print(Fore.MAGENTA + f"[FOLDER] .")
        if os.path.split(dir)[0] != dir:
            print(Fore.MAGENTA + f"[FOLDER] .." + Fore.WHITE)

        for folder in folders:
            print(Fore.MAGENTA + f"[FOLDER] {folder}" + Fore.WHITE)

        for file in files:
            print(f"[FILE]   {file}")

        action = input(Fore.WHITE + "\nДействие (:q - выйти из режима выбора): ")
        match action:
            case ":q":
                return ""
            case _:
                newPath = os.path.abspath(os.path.join(dir, action))
                if os.path.exists(newPath):
                    if os.path.isdir(newPath):
                        try:
                            os.listdir(newPath)
                            dir = newPath
                        except:
                            pass
                    else:
                        return newPath
                else:
                    if (
                        input(
                            Fore.YELLOW
                            + "Папки или файла с таким названием не существует.\nЖелаете создать новый файл? (y/N): "
                            + Fore.WHITE
                        ).lower()
                        == "y"
                    ):
                        open(newPath, "w+", encoding="UTF-8").close()
                        return newPath


def initFile(file: str):
    clear()
    printLog("База данных инициализирована!")
    open(file, "w+").close()

    while input("Хотите создать новую запись? (Y/n): ").lower() != "n":
        clear()
        printLog("База данных инициализирована!")
        addEntry(file)


def addEntry(file: str, pos=-1):
    with open(file, "rb+") as f:
        if pos == -1:
            f.seek(0, 2)
            pos = f.tell()
        else:
            pos = pos * (STRUCT.size + 1)
            f.seek(0, 2)
            if f.tell() < pos:
                pos = f.tell()
            f.seek(pos)

        obj = []
        for field in MODEL.values():
            success = False
            while not success:
                val = input(Fore.GREEN + field["name"] + ": " + Fore.WHITE)
                if val == "":
                    obj.append(field['default'])
                    break
                success, val = field["validator"](val)
                if not success:
                    printErr("Неверное значение!")
                    continue
                obj.append(val)
        b_obj = STRUCT.pack(*obj)

        last_line = f.readline()
        f.seek(pos)
        f.write(b_obj + b"\n")

        while last_line:
            cur_line, pos = f.readline(), pos + STRUCT.size + 1
            f.seek(pos)
            f.write(last_line)
            last_line = cur_line


def printSep(columnSizes):
    print("+" + "+".join(["-" * (el + 2) for el in columnSizes]) + "+")


def printValues(columnSizes, values):
    for i, el in enumerate(values):
        print(f"| {str(el):<{columnSizes[i]}} ", end="")
    print("|")
    printSep(columnSizes)


def printTable(file: str):
    columnSizes = [1] + [len(field["name"]) for field in MODEL.values()]
    cntOfEntries = -1
    with open(file, "rb") as f:
        for line in f:
            try:
                data = decodeEntry(line[:-1])
                cntOfEntries += 1
            except:
                printErr("Произошла ошибка при чтении БД!")
                return
            columnSizes[0] = max(columnSizes[0], len(str(cntOfEntries)))
            for i, el in enumerate(data):
                columnSizes[i + 1] = max(columnSizes[i + 1], len(str(el)))

    if cntOfEntries != -1:
        printSep(columnSizes)
        printValues(columnSizes, ["№"] + [field["name"] for field in MODEL.values()])

        with open(file, "rb") as f:
            cnt = 0
            for line in f:
                data = decodeEntry(line[:-1])
                printValues(columnSizes, [cnt] + data)
                cnt += 1
    else:
        printLog("БД не содержит ни одной записи!")


def getEntriesCount(file: str):
    with open(file, "rb") as f:
        cntOfEntries = 0
        for line in f:
            try:
                decodeEntry(line[:-1])
                cntOfEntries += 1
            except:
                printErr("Произошла ошибка при чтении БД!")
                return 0
    return cntOfEntries


def deleteEntry(file: str, pos):
    pos = pos * (STRUCT.size + 1)
    with open(file, "rb+") as f:
        
        f.seek(pos + STRUCT.size + 1)
        next_line = f.readline()
        while next_line:
            f.seek(pos)
            f.write(next_line)
            pos += STRUCT.size + 1
            f.seek(pos + STRUCT.size + 1)
            next_line = f.readline()
        f.seek(0, 2)
        f.seek(f.tell() - STRUCT.size - 1)
        f.truncate()


def findEntry(file: str, **kwargs):
    columnSizes = [1] + [len(field["name"]) for field in MODEL.values()]
    cntOfEntries = -1
    with open(file, "rb") as f:
        for line in f:
            try:
                data = decodeEntry(line[:-1])
            except:
                printErr("Произошла ошибка при чтении БД!")
                return

            flag = True
            for field in kwargs.keys():
                if field in MODEL.keys():
                    if data[MODEL[field]["offset"]] != kwargs[field]:
                        flag = False

            if flag:
                cntOfEntries += 1
                columnSizes[0] = max(columnSizes[0], len(str(cntOfEntries)))
                for i, el in enumerate(data):
                    columnSizes[i + 1] = max(columnSizes[i + 1], len(str(el)))

    if cntOfEntries != -1:
        printSep(columnSizes)
        printValues(columnSizes, ["№"] + [field["name"] for field in MODEL.values()])
        with open(file, "rb") as f:
            cnt = 0
            for line in f:
                data = decodeEntry(line[:-1])

                flag = True
                for field in kwargs.keys():
                    if field in MODEL.keys():
                        if data[MODEL[field]["offset"]] != kwargs[field]:
                            flag = False

                if flag:
                    printValues(columnSizes, [cnt] + data)
                    cnt += 1
    else:
        printLog("Не найдено ни одной записи!")


def pause():
    os.system("pause > nul")


def clear():
    os.system("cls")


def printErr(*args, **kwargs):
    print(Fore.RED, end="")
    print(*args, **kwargs)
    print(Fore.WHITE, end="")


def printLog(*args, **kwargs):
    print(Fore.CYAN, end="")
    print(*args, **kwargs)
    print(Fore.WHITE, end="")


if __name__ == "__main__":
    exec(open("main.py", encoding="UTF-8").read())
