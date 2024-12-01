class SquareMatrix:

    def __init__(self):
        self.__data = [[0]]  # __data is private

    def __len__(self):
        return len(self.__data)

    def set_matrix(self, _data):
        is_square = True
        _n = len(_data)
        for i in _data:
            if len(i) != _n:
                is_square = False
        if is_square:
            self.__data = _data
        return

    def set_matrix_from_string(self, _string, add='-'):
        from math import ceil
        _n = int(ceil(len(_string) ** 0.5))
        _n = _n + _n % 2
        self.__data = [[''] * _n for _ in range(_n)]
        for i in range(_n):
            for j in range(_n):
                if _n * i + j <= len(_string) - 1:
                    self.__data[i][j] = _string[_n * i + j]
                else:
                    self.__data[i][j] = add
        return

    def get_matrix(self):
        return self.__data

    def reduce_matrix(self):
        from functools import reduce
        return reduce(lambda x, y: x + reduce(lambda a, b: a + str(b), y, ''), self.__data, '')

    def rotate_90(self, _n, shift_i=0, shift_j=0):
        for i in range(_n):
            for j in range(i, _n - i - 1):
                tmp, ci, cj = self.__data[i + shift_i][j + shift_j], i, j  # current i and current j variable
                for _ in range(4):
                    self.__data[cj + shift_i][_n - ci - 1 + shift_j], tmp = (
                        tmp, self.__data[cj + shift_i][_n - ci - 1 + shift_j])
                    ci, cj = cj, _n - ci - 1
        return

    def rotate_180(self, _n, shift_i=0, shift_j=0):
        for i in range(_n // 2):
            for j in range(_n):
                self.__data[_n - i - 1 + shift_i][_n - j - 1 + shift_j], self.__data[i + shift_i][j + shift_j] = (
                    self.__data[i + shift_i][j + shift_j], self.__data[_n - i - 1 + shift_i][_n - j - 1 + shift_j])
        if _n % 2 == 1:
            for j in range(_n // 2):
                self.__data[_n // 2 + shift_i][_n - j - 1 + shift_j], self.__data[_n // 2 + shift_i][j + shift_j] = (
                    self.__data[_n // 2 + shift_i][j + shift_j], self.__data[_n // 2 + shift_i][_n - j - 1 + shift_j])
        return

    def rotate_270(self, _n, shift_i=0, shift_j=0):
        for i in range(_n):
            for j in range(i, _n - i - 1):
                tmp, ci, cj = self.__data[i + shift_i][j + shift_j], i, j  # current i and current j variable
                for _ in range(4):
                    self.__data[_n - cj - 1 + shift_i][ci + shift_j], tmp = (
                        tmp, self.__data[_n - cj - 1 + shift_i][ci + shift_j])
                    ci, cj = _n - cj - 1, ci
        return self.__data

    def generate_key(self, _n):
        from random import randint
        self.__data = [[''] * (2 * _n) for _ in range(2 * _n)]
        for i in range(_n):
            for j in range(_n):
                ri = randint(1, 4)
                self.__data[i][j] = str(int(1 == ri))
                self.__data[i][j + _n] = str(int(2 == ri))
                self.__data[i + _n][j + _n] = str(int(3 == ri))
                self.__data[i + _n][j] = str(int(4 == ri))

        self.rotate_90(_n, 0, _n)
        self.rotate_180(_n, _n, _n)
        self.rotate_270(_n, _n, 0)
        return


def encode(key, message, add='-'):
    n = len(key)
    result = [['']*n for _ in range(n)]
    pos = 0
    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if key.get_matrix()[i][j] == '1':
                    if pos <= len(message) - 1:
                        result[i][j] = message[pos]
                        pos += 1
                    else:
                        result[i][j] = add
        key.rotate_90(n)
    ans = SquareMatrix()
    ans.set_matrix(result)
    return ans


def decode(key, message):
    n = len(key)
    m = len(message)
    if m != n:
        return -1
    ans = ''
    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if key.get_matrix()[i][j] == '1':

                    ans += message.get_matrix()[i][j]
                    key.rotate_90(n)
        return ans


mode = '0'
while mode != '5':
    mode = input('Enter mode\n>1 - encode message with user key\n>2 - encode message with random key'
                 '\n>3 - decode message\n>4 - create key by n\n>5 - exit\n')
    while mode != '1' and mode != '2' and mode != '3' and mode != '4' and mode != '5':
        mode = input('Enter correct mode!\n>1 - encode message with user key\n>2 - encode message with random key'
                     '\n>3 - decode message\n>4 - create key by n\n>5 - exit\n')

    if mode == '1':

        mes = input('Enter a message to encode: ')

        k = SquareMatrix()
        k.set_matrix_from_string(input('Enter a key: '))

        res = encode(k, mes)

        print('Encoded message:', res.reduce_matrix())

    elif mode == '2':

        mes = input('Enter a message to encode: ')

        from math import ceil
        k = SquareMatrix()
        k.generate_key(int(ceil((len(mes)/4)**0.5)))

        res = encode(k, mes)

        print('Encoded message:', res.reduce_matrix())
        print('Used key:', k.reduce_matrix())

    elif mode == '3':

        k = SquareMatrix()
        k.set_matrix_from_string(input('Enter a key: '))

        mes = SquareMatrix()
        mes.set_matrix_from_string(input('Enter message to decode: '))

        res = decode(k, mes)
        if res != -1:
            print('Decoded message:', res)
        else:
            print('Invalid data')

    elif mode == '4':

        from math import ceil
        k = SquareMatrix()
        k.generate_key(int(ceil((int(input('Enter maximum string length: '))/4)**0.5)))

        print(k.reduce_matrix())