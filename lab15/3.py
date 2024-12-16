import struct
from colorama import Fore


with open("3.bin", "wb") as file:
    print("Введите числа (enter - выйти):")
    while True:
        try:
            enter = input()
            if enter == "":
                break
            file.write(struct.pack("i", int(enter)))
        except:
            print(Fore.RED + "Неверное число!" + Fore.WHITE)

with open("3.bin", "rb+") as file:
    file.seek(0, 2)
    size = file.tell() // 4
    print(size)

    def heaplify(size, i):
        largest = i
        next1, next2 = i * 2 + 1, i * 2 + 2

        file.seek(largest * 4)
        el_largest = el_i = struct.unpack("i", file.read(4))[0]

        if next1 < size:
            file.seek(next1 * 4)
            el_next1 = struct.unpack("i", file.read(4))[0]
            if el_next1 > el_largest:
                largest = next1
                el_largest = el_next1

        if next2 < size:
            file.seek(next2 * 4)
            el_next2 = struct.unpack("i", file.read(4))[0]
            if el_next2 > el_largest:
                largest = next2
                el_largest = el_next2

        if largest != i:
            file.seek(i * 4)
            file.write(struct.pack("i", el_largest))
            file.seek(largest * 4)
            file.write(struct.pack("i", el_i))
            return heaplify(size, largest)

    for i in range(size - 1, -1, -1):
        heaplify(size, i)

    for _ in range(size):
        file.seek((size - 1) * 4)
        el_s = struct.unpack("i", file.read(4))[0]
        file.seek(0)
        el_2 = struct.unpack("i", file.read(4))[0]
        file.seek(0)
        file.write(struct.pack("i", el_s))
        file.seek((size - 1) * 4)
        file.write(struct.pack("i", el_2))
        size -= 1
        heaplify(size, 0)


print("Измененный бинарный файл:")
with open("3.bin", "rb") as file:
    line = file.read(4)
    while line:
        print(struct.unpack(f"i", line)[0])
        line = file.read(4)
