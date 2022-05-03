""" 
Given the head of a singly linked list and an integer k, 
split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: 
no two parts should have a size differing by more than one. 
This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, 
and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

>>> Input: head = [1,2,3], k = 5
>>> Output: [[1],[2],[3],[],[]]

>>> Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
>>> Output: [[1,2,3,4],[5,6,7],[8,9,10]]
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]: ... 