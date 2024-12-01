from math import sqrt, ceil
from random import choice, randint

text = "вы любите розы а я на них срал"
alphabet = " абвгдеёжзийклмнопрстуфхцчшщьыъэюя"

# text = text.replace(" ", "")
n = ceil(sqrt(len(text)))

mask = [[False]*2*n for _ in range(2*n)]
matrix = [[choice(alphabet) for _ in range(2*n)] for _ in range(2*n)]

# получение маски
for y in range(n):
    for x in range(n):
        match randint(0, 3):
            case 0:
                mask[y][x] = True
            case 1:
                mask[x][2*n-y-1] = True
            case 2:
                mask[2*n-y-1][2*n-x-1] = True
            case 3:
                mask[2*n-x-1][y] = True

# шифрование по маске
for y, line in enumerate(mask):
    for x, el in enumerate(line):
        if el:
            if len(text) != 0:
                matrix[y][x] = text[0]
                text = text[1:]

print(*matrix, sep='\n')

# расшифровка по маске
t = ""
for y, line in enumerate(mask):
    for x, el in enumerate(line):
        if el:
            t += matrix[y][x]

print(t)