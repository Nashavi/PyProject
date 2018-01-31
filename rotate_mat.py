def rotate_90(matrix):
    n = len(matrix)
    for layer in range((n + 1) // 2):
        for index in range(layer, n - 1 - layer, 1):
            matrix[layer][index], matrix[n - 1 - index][layer], \
            matrix[index][n - 1 - layer], matrix[n - 1 - layer][n - 1 - index] = \
                matrix[n - 1 - index][layer], matrix[n - 1 - layer][n - 1 - index], \
                matrix[layer][index], matrix[index][n - 1 - layer]
    return matrix

import unittest

class MyTest(unittest.TestCase):
    def test_rotate_matrix_right_90(self):
        input_matrix = [[0, 2, 4, 6], [-1, 1, 3, 5], [-2, 0, 2, 4], [-3, -1, 1, 3]]
        correct_rotated_matrix = [[-3, -2, -1, 0], [-1, 0, 1, 2], [1, 2, 3, 4], [3, 4, 5, 6]]
        self.assertSequenceEqual(rotate_90(input_matrix), correct_rotated_matrix)


if __name__ == "__main__":
    unittest.main()
