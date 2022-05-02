"""
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

    The rank is an integer starting from 1.
    If two elements p and q are in the same row or column, then:
        If p < q then rank(p) < rank(q)
        If p == q then rank(p) == rank(q)
        If p > q then rank(p) > rank(q)
    The rank should be as small as possible.

>>> Input: matrix = [[1,2],[3,4]]
>>> Output: [[1,2],[2,3]]

>>> Input: matrix = [[7,7],[7,7]]
>>> Output: [[1,1],[1,1]]
"""

from typing import List
from collections import defaultdict


## Using Union Find algorithm ## 
def matrix_rank_transform(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    rank = [0] * (m+n)
    d = defaultdict(list)
    
    for i in range(m):
        for j in range(n):
            d[matrix[i][j]].append((i, j))
            
    def _find(i):
        if p[i] != i:
            p[i] = _find(p[i])
        return p[i]
    
    def _union(i, j):
        p_i, p_j = _find(i), _find(j)
        p[p_i] = p_j
        new_rank[p_j] = max(new_rank[p_i], new_rank[p_j])
    
    for e in sorted(d):
        p = list(range(m+n))
        new_rank = rank[:]
        
        for i, j in d[e]:
            _union(i, m+j)
        
        for i, j in d[e]:
            rank[i] = rank[m+j] = matrix[i][j] = new_rank[_find(i)] + 1
    
    return matrix 

#### TestCase 

import unittest

class TestCase(unittest.TestCase):
    def test_matrix_increase_rank_number(self):
        matrix = [[1, 2],[3, 4]]
        self.assertEqual(matrix_rank_transform(matrix), [
            [1, 2], 
            [2, 3]
        ])

    def test_matrix_with_all_rank_1(self):
        matrix = [
            [7, 7], 
            [7, 7]
        ]

        self.assertEqual(matrix_rank_transform(matrix), [
            [1, 1], 
            [1, 1]
        ])

    def test_matrix_rank_transform(self):
        matrix = [
            [20, -21, 14],
            [-19, 4, 19],
            [22, -47, 24],
            [-19, 4, 19]
        ]

        self.assertEqual(matrix_rank_transform(matrix), [
            [4, 2, 3], 
            [1, 3, 4], 
            [5, 1, 6], 
            [1, 3, 4]
        ])

if __name__ == '__main__':
    unittest.main()