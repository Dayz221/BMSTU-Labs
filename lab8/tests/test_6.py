import unittest
from lab8.ex6 import main


class TestMatrixTranspose(unittest.TestCase):
    def test_square_matrix(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected = [[1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]]
        result = main(matrix, 3, 3)
        self.assertEqual(result, expected)

    def test_rectangle_matrix(self):
        matrix = [[1, 2],
                  [3, 4],
                  [5, 6]]
        expected = [[1, 3, 5],
                    [2, 4, 6]]
        result = main(matrix, 3, 2)
        self.assertEqual(result, expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        result = main(matrix, 0, 0)
        self.assertEqual(result, expected)

    def test_single_element_matrix(self):
        matrix = [[42]]
        expected = [[42]]
        result = main(matrix, 1, 1)
        self.assertEqual(result, expected)

    def test_matrix_with_negative_numbers(self):
        matrix = [[-1, -2, -3],
                  [-4, -5, -6]]
        expected = [[-1, -4],
                    [-2, -5],
                    [-3, -6]]
        result = main(matrix, 2, 3)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
