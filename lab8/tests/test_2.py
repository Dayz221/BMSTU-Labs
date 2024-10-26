import unittest
from lab8.ex2 import main


class TestMainFunction(unittest.TestCase):
    def test_no_negative_elements(self):
        # Матрица без отрицательных элементов
        X = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        m = 3
        result = main(X, m)
        self.assertEqual(result, X)  # Ожидается, что матрица не изменится

    def test_all_negative_elements(self):
        # Матрица, где все элементы отрицательные
        X = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        m = 3
        result = main(X, m)
        self.assertEqual(result, X)  # Ожидается, что матрица не изменится

    def test_mixed_elements(self):
        # Матрица с положительными и отрицательными элементами
        X = [
            [1, -1, 2, -2],
            [3, 4, -3, -4],
            [-5, 6, 7, -8]
        ]
        m = 3
        result = main(X, m)
        self.assertEqual(result, X)  # Ожидается, что матрица не изменится

    def test_single_row(self):
        # Матрица из одной строки
        X = [[-1, -2, -3]]
        m = 1
        result = main(X, m)
        self.assertEqual(result, X)  # Ожидается, что матрица не изменится

    def test_no_negative_swap(self):
        # Проверка, что функция правильно определяет строки, если обмен не требуется
        X = [
            [1, -2, 3],
            [4, 5, -6],
            [-1, -1, 8]
        ]
        m = 3
        result = main(X, m)
        self.assertEqual(result[0], [-1, -1, 8])  # Строка с наибольшим количеством отрицательных элементов
        self.assertEqual(result[2], [1, -2, 3])  # Строка с наименьшим количеством отрицательных элементов


if __name__ == "__main__":
    unittest.main()
