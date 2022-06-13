""" triangle 
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.

>>> Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
>>> Output: 11

>>> Input: triangle = [[-10]]
>>> Output: -10
"""
from typing import List
import unittest

def triangle_list_dp(triangle: List[List[int]]) -> int:
    if not triangle:
        return 
    
    res = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])): 
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    
    return res[0]


def triangle_list_memoization(triangle: List[List[int]]) -> int:
    nums = {}

    def dfs(i: int, row: int):
        if row >= len(triangle):
            return 0 
        elif (i, row) in nums:
            return nums[(i, row)]
    
        nums[(i, row)] = triangle[row][i] + min(dfs(i, row+1), dfs(i+1, row+1))
        return nums[(i, row)]
    
    return dfs(0, 0)

class test(unittest.TestCase):
    def test_example_1(self):
        _list = [[2],[3,4],[6,5,7],[4,1,8,3]]
        input = triangle_list_dp(_list)
        expected = 11

        self.assertEqual(input, expected)
    
    def test_example_2(self):
        _list = [[-10]]
        input = triangle_list_dp(_list)
        expected = -10

        self.assertEqual(input, expected)
        
    def test_example_1_memo(self):
        _list = [[2],[3,4],[6,5,7],[4,1,8,3]]
        input = triangle_list_memoization(_list)
        expected = 11

        self.assertEqual(input, expected)
    
    def test_example_2_memo(self):
        _list = [[-10]]
        input = triangle_list_memoization(_list)
        expected = -10

        self.assertEqual(input, expected)
if __name__ == '__main__':
    unittest.main()