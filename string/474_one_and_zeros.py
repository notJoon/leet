""" One and zeros 
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

>>> Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
>>> Output: 4
"""
from collections import defaultdict
from typing import List
import unittest

def one_and_zeros(strs: List[str], m: int, n: int) -> int:
    strs = [(s.count('0'), s.count('1')) for s in strs]

    dp = defaultdict(int)
    dp[0, 0] = 0

    for i0, i1 in strs:
        for (j0, j1), count in list(dp.items()):
            if (i0 + j0 <= m) and (i1 + j1 <= n):
                key = (i0+j0, i1+j1)
                dp[key] = max(count+1, dp[key])
    
    return max(dp.values())

class Test(unittest.TestCase):
    def test_example_1(self):
        strs = ["10","0001","111001","1","0"]
        m = 5
        n = 3
        expected = 4
        self.assertEqual(one_and_zeros(strs, m, n), expected)

    def test_example_2(self):
        strs = ["10","0","1"]
        m = 1
        n = 1
        expected = 2
        self.assertEqual(one_and_zeros(strs, m, n), expected)



if __name__ == '__main__':
    unittest.main()