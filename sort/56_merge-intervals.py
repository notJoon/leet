"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, 
and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if l and i[0] <= l[-1][1]:
                l[-1][1] = max(l[-1][1], i[1])
        
            else:
                l += [i]
        
        return l 