""" 
Given an array of integers arr, 
a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1

>>> Input: arr = [2,2,3,4]
>>> Output: 2

>>> Input: arr = [1,2,2,3,3,3]
>>> Output: 3

"""

from typing import List


def find_lucky_number(arr: List[int]) -> int:
    num_counts = {}
    for n in arr:
        num_counts[n] = num_counts.get(n, 0) + 1
        is_lucky = {k for k, v in num_counts.items() if k == v}

    return max(is_lucky) if is_lucky else -1


### Test 
import unittest 

class Test(unittest.TestCase):
    def one_lucky_number(self):
        arr = [2,2,3,4]
        self.assertEqual(find_lucky_number(arr), 2)

    def multiple_lucky_number(self):
        arr = [1,2,2,3,3,3]
        self.assertEqual(find_lucky_number(arr), 3)

    def lucky_number_dosent_exist(self):
        arr = [2,2,2,3,3]
        self.assertEqual(find_lucky_number(arr), -1)


if __name__ == '__main__':
    unittest.main()