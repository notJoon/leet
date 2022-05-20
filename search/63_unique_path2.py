""" Unique Path II
You are given an m x n integer array grid. 
There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109

>>> Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
>>> Output: 2

>>> Input: obstacleGrid = [[0,1],[0,0]]
>>> Output: 1
"""

from typing import List

def unique_path(obstacle_grid: List[List[int]]) -> int:
    ## except conditions
    if obstacle_grid[0][0] == 1 or obstacle_grid[-1][-1] == 1:
        return 0 
    
    matrix = [[0] * range(len(obstacle_grid[0])) for _ in range(len(obstacle_grid))]
    matrix[0][0] = 1 ## init position 

    for row in range(len(obstacle_grid)):
        for col in range(len(obstacle_grid[0])):
            if obstacle_grid[row][col] == 0:
                matrix[row][col] += matrix[row-1][col] if row >= 0 else 0
                matrix[row][col] += matrix[row][col-1] if col-1 >= 0 else 0
    
    return matrix[-1][-1]

import unittest
class Test(unittest.TestCase):
    
    input: List[int]

    def except_condition_1x1(self):
        input = [[1]]
        self.assertEqual(unique_path(input), 0)
    
    def except_conditon_last_elemet_is_1(self):
        input = [
            [0, 0], 
            [0, 1]
        ]
        self.assertEqual(unique_path(input), 0)

    def unique_path_example_1(self):
        input = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(unique_path(input), 2)
        
    def unique_path_example_2(self):
        input = [
            [0, 1],
            [0, 0]
        ]
        self.assertEqual(unique_path(input), 1)

    def unique_path_complex(self):
        input = [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(unique_path(input), 5)

if __name__ == "__main__":
    unittest.main()
