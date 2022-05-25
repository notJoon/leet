""" Russian Doll Envelopes
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
represents the width and the height of an envelope.

One envelope can fit into another 
if and only if both the width and height of one envelope are greater 
than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

>>> Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
>>> Output: 3

>>> Input: envelopes = [[1, 1],[1,1],[1,1],[1,1]]
>>> Output: 1
"""
from typing import List
import unittest

def russian_doll_envelopes(envelopes: List[List[int]]) -> int:
    n = len(envelopes)
    if n <= 1:
        return n 
    
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    tails = [0]*n
    size = 0
    for _, env in envelopes: 
        l, r = 0, size-1
        while (l <= r):
            mid = (l+r)//2 
            if tails[mid] >= env:
                r = mid - 1
            else:
                l = mid + 1
        tails[l] = env
        size = max(size, l+1)
    return size 

class test(unittest.TestCase):
    def test_example_1(self):
        envelopes = [[5,4],[6,4],[6,7],[2,3]]
        input = russian_doll_envelopes(envelopes)
        expect = 3
        self.assertEqual(input, expect)
    
    def test_example_2(self):
        envelopes = [[1,1],[1,1],[1,1],[1,1]]
        input = russian_doll_envelopes(envelopes)
        expect = 1
        self.assertEqual(input, expect)

    def test_example_3(self):
        envelopes = [[5,4]]
        input = russian_doll_envelopes(envelopes)
        expect = 1
        self.assertEqual(input, expect)

if __name__ == '__main__':
    unittest.main()