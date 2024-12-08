import os
from colorama import Fore
from dbModel import DB_MODEL


def changeFile(dir: str) -> str:
    while True:
        clear()
        folders: list[str] = []
        files: list[str] = []

        printText("Текущая директория: " + Fore.CYAN + dir + "\n")

        for entry in os.listdir(dir):
            if os.path.isdir(os.path.join(dir, entry)):
                folders.append(entry)
            elif os.path.isfile(os.path.join(dir, entry)):
                files.append(entry)

        print(Fore.MAGENTA + f"[FOLDER] .")
        if os.path.split(dir)[0] != dir:
            print(Fore.MAGENTA + f"[FOLDER] ..")

        for folder in folders:
            print(Fore.MAGENTA + f"[FOLDER] {folder}")

        for file in files:
            printText(f"[FILE]   {file}")

        action = input(Fore.WHITE + "\nДействие (:q - выйти из режима выбора): ")
        match action:
            case ":q":
                return ""
            case _:
                newPath = os.path.abspath(os.path.join(dir, action))
                if os.path.exists(newPath):
                    if os.path.isdir(newPath):
                        dir = newPath
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


def convert(type, value):
    try:
        arg = type(value)
        return (True, arg)
    except:
        return (False, None)


def initDataBase(file: str):
    with open(file, "w+", encoding="UTF-8") as f:
        while True:
            clear()
            printLog("База данных создана!")
            if input(Fore.WHITE + "Добавить запись? (Y/n): ").lower() != "n":
                obj = ["" for _ in range(len(DB_MODEL.keys()))]
                for field in DB_MODEL.values():
                    while True:
                        val = input(
                            Fore.GREEN
                            + f"{field['name']} ({field['type'].__class__.__name__}): "
                            + Fore.WHITE
                        )
                        if not val.strip():
                            obj[field["offset"]] = str(field["default"])
                            break
                        success, converted = convert(field["type"], val)
                        if success:
                            obj[field["offset"]] = str(converted)
                            break
                        else:
                            printErr("Введено неверное значение!")
                f.write(";".join(obj) + "\n")
            else:
                break


def printTableHead(columnSizes):
    print("+" + "+".join(["-" * (el + 2) for el in columnSizes]) + "+")

    for i, el in enumerate([el["name"] for el in DB_MODEL.values()]):
        print(f"| {el:^{columnSizes[i]}} ", end="")
    print("|")
    print("+" + "+".join(["-" * (el + 2) for el in columnSizes]) + "+")


def printDataBase(file: str):
    clear()
    print(Fore.WHITE + "База данных: " + Fore.CYAN + file + Fore.WHITE)
    columnSizes = [len(el["name"]) for el in DB_MODEL.values()]
    with open(file, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if line:
                row = line.split(";")

                if len(row) != len(DB_MODEL.keys()):
                    printErr("База данных недействительна!")
                    return

                for i, el in enumerate(row):
                    columnSizes[i] = max(columnSizes[i], len(el))

    printTableHead(columnSizes)

    with open(file, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if line:
                row = line.split(";")
                for i, el in enumerate(row):
                    print(f"| {el:<{columnSizes[i]}} ", end="")
                print("|")
                print("+" + "+".join(["-" * (el + 2) for el in columnSizes]) + "+")


def addDocument(file: str):
    clear()
    printLog("Добавить объект в базу данных")
    with open(file, "a", encoding="UTF-8") as f:
        obj = ["" for _ in range(len(DB_MODEL.keys()))]
        for field in DB_MODEL.values():
            while True:
                val = input(
                    Fore.GREEN + f"{field['name']} ({field['type']}): " + Fore.WHITE
                )
                if not val.strip():
                    obj[field["offset"]] = str(field["default"])
                    break
                success, converted = convert(field["type"], val)
                if success:
                    obj[field["offset"]] = str(converted)
                    break
                else:
                    printErr("Введено неверное значение!")
        f.write(";".join(obj) + "\n")


def findElement(file: str, **kwargs):
    clear()
    answ = []
    with open(file, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if line:
                row = line.split(";")
                if len(row) != len(DB_MODEL.keys()):
                    printErr("База данных недействительна!")
                    return
                obj = {}
                for key, field in DB_MODEL.items():
                    success, obj[key] = convert(field["type"], row[field["offset"]])
                    if not success:
                        printErr("База данных недействительна!")
                        return
                flag = True
                for key in kwargs:
                    if kwargs[key] != obj[key]:
                        flag = False
                if flag: 
                    answ.append(obj)

    columnSizes = [len(el["name"]) for el in DB_MODEL.values()]

    for row in answ:
        for i, el in enumerate(row.values()):
            columnSizes[i] = max(columnSizes[i], len(str(el)))

    printTableHead(columnSizes)

    for row in answ:
        for i, el in enumerate(row.values()):
            print(f"| {el:<{columnSizes[i]}} ", end="")
        print("|")
        print("+" + "+".join(["-" * (el + 2) for el in columnSizes]) + "+")


def pause():
    os.system("pause > nul")


def clear():
    os.system("cls")


def printText(*args, **kwargs):
    print(Fore.WHITE, end="")
    print(*args, **kwargs)


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
