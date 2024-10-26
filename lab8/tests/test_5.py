import unittest
from lab8.ex5 import main


class TestMatrixFunctions(unittest.TestCase):
    def test_square_matrix_with_positive_values(self):
        X = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        m, n = 3, 3
        min_el, max_el = main(X, m, n)
        self.assertEqual(min_el, 6)  # Минимальное под побочной диагональю
        self.assertEqual(max_el, 6)  # Максимальное над главной диагональю

    def test_square_matrix_with_negative_values(self):
        X = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        m, n = 3, 3
        min_el, max_el = main(X, m, n)
        self.assertEqual(min_el, -9)  # Минимальное под побочной диагональю
        self.assertEqual(max_el, -2)  # Максимальное над главной диагональю

    def test_square_matrix_with_mixed_values(self):
        X = [
            [0, -2, 5],
            [4, 3, -1],
            [-3, 2, 1]
        ]
        m, n = 3, 3
        min_el, max_el = main(X, m, n)
        self.assertEqual(min_el, -1)  # Минимальное под побочной диагональю
        self.assertEqual(max_el, 5)  # Максимальное над главной диагональю

    def test_square_matrix_with_no_valid_elements(self):
        X = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        m, n = 3, 3
        min_el, max_el = main(X, m, n)
        self.assertEqual(min_el, 0)  # Не должно быть минимального под побочной
        self.assertEqual(max_el, 0)  # Не должно быть максимального над главной


if __name__ == "__main__":
    unittest.main()
