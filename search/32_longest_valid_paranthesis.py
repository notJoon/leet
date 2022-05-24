""" Longest Valid Parentheses
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

>>> Input: s = "(()"
>>> Output: 2

>>> Input: s = ")()())"
>>> Output: 4

>>> Input: s = ""
>>> Output: 0

>>> Input: s = ")("
>>> Output: 0
"""
import unittest

def longest_valid_parenthesis(s: str) -> int:
    valid = [-1]
    max_len = 0

    if not s:
        return 0 
    
    for k, v in enumerate(s):
        if v == '(':
            valid.append(k)
        else:
            valid.pop()

            if not valid:
                valid.append(k)
            else:
                max_len = max(max_len, k-valid[-1])
    return max_len 


class Test(unittest.TestCase):
    def test_example_1(self):
        s = "(()"
        expect = 2
        self.assertEqual(longest_valid_parenthesis(s), expect)
    
    def test_example_2(self):
        s = "(("
        expect = 0
        self.assertEqual(longest_valid_parenthesis(s), expect)

    def test_example_3(self):
        s = ")()())"
        expect = 4
        self.assertEqual(longest_valid_parenthesis(s), expect)

if __name__ == '__main__':
    unittest.main()