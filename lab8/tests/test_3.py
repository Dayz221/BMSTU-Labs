import unittest
from lab8.ex3 import main


class TestMainFunction(unittest.TestCase):
    def test_column_with_max_primes(self):
        # Матрица с простыми числами в столбцах
        X = [
            [2, 4, 5],
            [3, 8, 7],
            [5, 10, 11]
        ]
        m, n = 3, 3
        idx, cnt = main(X, m, n)
        self.assertEqual(idx, 0)
        self.assertEqual(cnt, 3)

    def test_no_primes(self):
        # Матрица без простых чисел
        X = [
            [4, 6, 8],
            [10, 12, 14],
            [16, 18, 20]
        ]
        m, n = 3, 3
        idx, cnt = main(X, m, n)
        self.assertEqual(idx, 0)  # При отсутствии простых чисел возвращается первый столбец (индекс 0)
        self.assertEqual(cnt, 0)

    def test_equal_primes_in_columns(self):
        # Все столбцы содержат одинаковое количество простых чисел
        X = [
            [2, 3, 5],
            [7, 5, 11],
            [13, 17, 19]
        ]
        m, n = 3, 3
        idx, cnt = main(X, m, n)
        self.assertEqual(idx, 0)  # Если количество простых одинаково, возвращается первый столбец
        self.assertEqual(cnt, 3)

    def test_single_column(self):
        # Матрица с одним столбцом
        X = [
            [2],
            [3],
            [4]
        ]
        m, n = 3, 1
        idx, cnt = main(X, m, n)
        self.assertEqual(idx, 0)  # Один столбец, индекс всегда будет 0
        self.assertEqual(cnt, 2)

    def test_single_row(self):
        # Матрица с одной строкой
        X = [[2, 3, 5, 8]]
        m, n = 1, 4
        idx, cnt = main(X, m, n)
        self.assertEqual(idx, 0)  # Первый столбец с простым числом возвращается первым
        self.assertEqual(cnt, 1)

    def test_mixed_elements(self):
        # Матрица с положительными, отрицательными числами и нулями
        X = [
            [2, -3, 5],
            [0, 5, -11],
            [17, 1, 2]
        ]
        m, n = 3, 3
        idx, cnt = main(X, m, n)
        self.assertEqual(idx, 0)  # Первый столбец имеет больше всего простых чисел (2, 17)
        self.assertEqual(cnt, 2)


if __name__ == "__main__":
    unittest.main()
