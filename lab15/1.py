import struct
from colorama import Fore

with open("1.bin", "wb") as file:
    print("Введите числа (enter - выйти):")
    while True:
        try:
            enter = input()
            if enter == "":
                break
            file.write(struct.pack("i", int(enter)))
        except:
            print(Fore.RED + "Неверное число!" + Fore.WHITE)


offset = 4
with open("1.bin", "rb+") as file:
    line = file.read(4)
    while line:
        el = struct.unpack("i", line)[0]
        if el < 0:
            offset += 4
            line = file.read(4)
            continue
        file.seek(-offset, 1)
        file.write(line)
        file.seek(offset - 4, 1)
        line = file.read(4)

    file.seek(-offset + 4, 2)
    file.truncate()


print("Измененный бинарный файл:")
with open("1.bin", "rb") as file:
    line = file.read(4)
    while line:
        print(struct.unpack("i", line)[0])
        line = file.read(4)
