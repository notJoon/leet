""" Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

>>> Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> Output: [[1,4,7],[2,5,8],[3,6,9]]

>>> Input: matrix = [[1,2,3],[4,5,6]]
>>> Output: [[1,4],[2,5],[3,6]]
"""
from typing import List
import unittest

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    m = len(matrix)
    n = len(matrix[0])

    transposed = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    
    return transposed

class test(unittest.TestCase):
    def test_example_1(self):
        input = [[1,2,3],[4,5,6],[7,8,9]]
        expect = [[1,4,7],[2,5,8],[3,6,9]]

        self.assertEqual(transpose_matrix(input), expect)

    def test_example_2(self):
        input = [[1,2,3],[4,5,6]]
        expect = [[1,4],[2,5],[3,6]]
        
        self.assertEqual(transpose_matrix(input), expect)

if __name__ == '__main__':
    unittest.main()