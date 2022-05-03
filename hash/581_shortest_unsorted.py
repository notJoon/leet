""" 
Given an integer array nums, you need to find one continuous subarray 
that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

>>> input: nums = [2, 6, 4, 8, 10, 9, 15]
>>> output: 5 

>>> input: nums = [1, 2, 3, 4]
>>> outputs: 0

>>> input: nums = [1]
>>> output: 0 
"""

from typing import List


def find_unsorted_subarray(nums: List[int]) -> int:
    """
    Args:
        nums (List[int]): given integer array

    Returns:
        int: shortest subarray's length 
    """
    start = -1 
    end = -2 

    for i, num in enumerate(sorted(nums)):
        if num != nums[i]:
            if start == -1:
                start = i 
            else:
                end = i 
    return end - start + 1 


###
import unittest

class Test(unittest.TestCase):
    def array_with_discountious_order(self):
        nums = [2, 6, 4, 8, 10, 9, 15]
        self.assertEqual(find_unsorted_subarray(nums), 5)
    
    def array_with_continous_order(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(find_unsorted_subarray(nums), 0)
    
    def array_only_have_one_item(self):
        nums = [1]
        self.assertEqual(find_unsorted_subarray(nums), 0)

if __name__ == '__main__':
    unittest.main()