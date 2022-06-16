""" Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

>>> input: s = "babad"
>>> output: "bab

"""
import unittest

def longest_palindrome(s: str) -> str:
    if not s:
        return ''
    
    n = len(s)
    start_position = 0
    maxlen = 1

    for i in range(n):
        right = i 

        while right < n and s[i] == s[right]:
            right += 1
        
        left = i - 1
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        
        total_len = right - left - 1
        if total_len > maxlen:
            maxlen = total_len
            start_position = left + 1

    return s[ start_position : start_position + maxlen]





class test(unittest.TestCase):
    def test_example_1(self):
        s = 'babad'
        expected = 'bab'
        self.assertEqual(longest_palindrome(s), expected)
    
    def test_example_2(self):
        s = 'cbbbaabbbd'
        expected = 'bbbaabbb'
        self.assertEqual(longest_palindrome(s), expected)

if __name__ == '__main__':
    unittest.main()