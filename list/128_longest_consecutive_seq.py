""" 128. Longest Consecutive Sequence
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

>>> input: [100,4,200,1,3,2]
>>> Output: 4
"""
import unittest
from typing import List

def longestConsecutive(nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                start, end = num, num
                while end + 1 in nums:
                    end += 1
                    
                max_len = max(max_len, end - start + 1)
        
        return max_len 

class test(unittest.TestCase):
    
    input: List[int]
    expect: int
    
    def test_example_1(self):
        input = [100,4,200,1,3,2]
        expect = 4
        self.assertEqual(longestConsecutive(input), expect)

    def test_example_2(self):
        input = [0,3,7,2,5,8,4,6,0,1]
        expect = 9
        self.assertEqual(longestConsecutive(input), expect)

if __name__ == '__main__':
    unittest.main()