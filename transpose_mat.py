def transpose(mat):
    l1 = []

    for i in range(len(mat[0])):
        l2 = []
        for j in range(len(mat)):
            l2.append(mat[j][i])
        l1.append(l2)

    return l1


import unittest

class MyTest(unittest.TestCase):
    def test_transpose(self):
        input_matrix = [[1,2,3],[4,5,6],[7,8,9]]
        correct_rotated_matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertSequenceEqual(transpose(input_matrix), correct_rotated_matrix)


if __name__ == "__main__":
    unittest.main()
