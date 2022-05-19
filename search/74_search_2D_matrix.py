""" Search a 2D matrix 
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    * Integers in each row are sorted from left to right.
    * The first integer of each row is greater than the last integer of the previous row.


>>> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
>>> Output: true

>>> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
>>> Output: false
"""
from typing import List


def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        if row[-1] >= target:
            return target in row 
    return False 

def use_linear_search(matrix: List[List[int]], target: int) -> bool:
    """ 
    treat 2D matrix as 1D List and do search 
    time complexity O(log(MN))
    """
    n = len(matrix[0])
    low, high = 0, len(matrix) * n

    while low < high:
        mid = (low + high) / 2 
        x = matrix[mid/n][mid%2]

        if x < target:
            low = mid + 1
        elif x > target:
            high = mid 
        else: 
            return True 
    
    return False 
        

def use_stair_case_search(matrix: List[List[int]], target: int) -> bool:
    """ 
    Staircase search
    Time Complexity O(M + N)
    """
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target: 
            return True 
        if target > matrix[row][col]:
            row += 1 
        else:
            col += 1

    return False 
        
