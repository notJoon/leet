""" Range Sum of BST
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high]

>>> input: root = [10,5,15,3,7,null,18], low = 7, high = 15
>>> output: 32

>>> input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
>>> output: 23
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque([root])
        node_sum, val = 0, 0
        
        while q:
            root = q.popleft()
            val = root.val
            
            if val >= low and val <= high:
                node_sum += val
            
            if val > low and root.left:
                q.append(root.left)
                
            if val < high and root.right:
                q.append(root.right)
        
        return node_sum