import unittest
from lab8.ex1 import main


class TestMainFunction(unittest.TestCase):
    def test_single_row(self):
        # Матрица из одной строки с одним элементом
        X = [[5]]
        m = 1
        self.assertEqual(main(X, m), 0)

    def test_multiple_rows_same_average(self):
        # Все строки имеют одинаковое среднее значение
        X = [
            [1, 2, 3],
            [3, 2, 1],
            [2, 2, 2]
        ]
        m = 3
        self.assertEqual(main(X, m), 0)  # Первая строка по умолчанию

    def test_multiple_rows_different_average(self):
        # Строка с наибольшим средним находится в середине
        X = [
            [1, 2, 3],
            [4, 5, 6],
            [1, 1, 1]
        ]
        m = 3
        self.assertEqual(main(X, m), 1)  # Вторая строка

    def test_negative_values(self):
        # Матрица с отрицательными значениями
        X = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-1, -1, -1]
        ]
        m = 3
        self.assertEqual(main(X, m), 2)  # Третья строка

    def test_large_matrix(self):
        # Проверка на корректность работы с большой матрицей
        X = [
            [i for i in range(100)] for _ in range(100)
        ]
        m = 100
        self.assertEqual(main(X, m), 0)


if __name__ == "__main__":
    unittest.main()
