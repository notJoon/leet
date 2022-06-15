""" Validate Binary Search Tree 

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

   * The left subtree of a node contains only nodes with keys less than the node's key.
   * The right subtree of a node contains only nodes with keys greater than the node's key.
   * Both the left and right subtrees must also be binary search trees.

>>> Input: root = [2,1,3]
>>> Output: true

>>> Input: root = [5,1,4,null,null,3,6]
>>> Output: false
"""
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_tree(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left_bound, right_bound) -> bool:
            if not node:
                return True 
            
            if not (node.val < right_bound and node.val > left_bound):
                return False 
            
            return (valid(node.left, left_bound, node.val) and 
                    valid(node.right, node.val, right_bound))
        
        return valid(root, float('-inf'), float('inf'))