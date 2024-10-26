import unittest
from lab8.ex4 import main


class TestColumnPermutation(unittest.TestCase):
    def test_matrix_with_positive_values(self):
        X = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        m, n = 3, 3
        expected = [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7]
        ]
        result = main(X, m, n)
        self.assertEqual(result, expected)

    def test_matrix_with_negative_values(self):
        X = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        m, n = 3, 3
        expected = [
            [-3, -2, -1],
            [-6, -5, -4],
            [-9, -8, -7]
        ]
        result = main(X, m, n)
        self.assertEqual(result, expected)

    def test_matrix_with_mixed_values(self):
        X = [
            [0, -2, 5],
            [4, 3, -1],
            [-3, 2, 1]
        ]
        m, n = 3, 3
        expected = [
            [5, -2, 0],
            [-1, 3, 4],
            [1, 2, -3]
        ]
        result = main(X, m, n)
        self.assertEqual(result, expected)

    def test_matrix_with_identical_columns(self):
        X = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        m, n = 3, 3
        expected = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = main(X, m, n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
