""" Palindromic Substrings 
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

>>> Input: s = "abc"
>>> Output: 3

>>> Input: s = "aaa"
>>> Output: 6
"""

from typing import List


def palindromic_substrings(s: str) -> int:
    assert 1 <= len(s) <= 1000

    n = len(s)
    dp = [[False]*n for _ in range(n)]

    if n == 1:
        return 1
    
    def find_sub(left: int, right: int) -> List:
        if left > right:
            return True 
        return dp[left][right]

    counter = 0
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                dp[i][j] = find_sub(i+1, j-1)

            if dp[i][j]:
                counter += 1
    return counter 

import unittest

class Test(unittest.TestCase):

    input: str 
    expected: int 

    def test_example_1(self):
        input = "abc"
        expected = 3
        self.assertEqual(palindromic_substrings(input), expected)
    
    def test_example_2(self):
        input = "a"
        expected = 1
        self.assertEqual(palindromic_substrings(input), expected)

    def test_example_3(self):
        input = "aaa"
        expected = 6
        self.assertEqual(palindromic_substrings(input), expected)
        
    def test_example_4(self):
        input = "abaaaa"
        expected = 13
        self.assertEqual(palindromic_substrings(input), expected)

if __name__ == "__main__":
    unittest.main()