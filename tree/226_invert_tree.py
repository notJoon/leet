""" Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

>>> Input: [4,2,7,1,3,6,9]
>>> Output: [4,7,2,9,6,3,1]
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 

        # swap nodes
        tmp = root.left 
        root.left = root.right
        root.right = tmp 

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root 