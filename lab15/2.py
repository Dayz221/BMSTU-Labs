import struct
from colorama import Fore

with open("2.bin", "wb") as file:
    print("Введите числа (enter - выйти):")
    while True:
        try:
            enter = input()
            if enter == "":
                break
            file.write(struct.pack("i", int(enter)))
        except:
            print(Fore.RED + "Неверное число!" + Fore.WHITE)

cnt = 0
cur_elem = -4
with open("2.bin", "rb+") as file:
    line = file.read(4)
    while line:
        el = struct.unpack("i", line)[0]
        if el % 2 == 1:
            cnt += 1
        cur_elem += 4
        line = file.read(4)

    for _ in range(cnt):
        file.write(b"\x00\x00\x00\x00")


offset = 4 * cnt
with open("2.bin", "r+b") as file:
    while cur_elem >= 0:
        file.seek(cur_elem)
        el = struct.unpack("i", file.read(4))[0]
        if el % 2 == 1:
            file.seek(cur_elem + offset)
            file.write(struct.pack("i", el * 2))
            file.seek(cur_elem + offset - 4)
            file.write(struct.pack("i", el))
            offset -= 4

        else:
            file.seek(cur_elem + offset)
            file.write(struct.pack("i", el))
        cur_elem -= 4


print("Измененный бинарный файл:")
with open("2.bin", "rb") as file:
    line = file.read(4)
    while line:
        print(struct.unpack(f"i", line)[0])
        line = file.read(4)
