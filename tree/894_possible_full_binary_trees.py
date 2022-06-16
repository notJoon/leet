""" All possible full binary tree(FBT)

Given an integer n, return a list of all possible full binary trees with n nodes. 
Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. 
You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.


>>> Input: n = 7
>>> Output: [[0,0,0,null,null,0,0,null,null,0,0],
            [0,0,0,null,null,0,0,0,0], 
            [0,0,0,0,0,0,0], 
            [0,0,0,0,0,null,null,null,null,0,0], 
            [0,0,0,0,0,null,null,0,0]]

>>> Input: n = 3
>>> Output: [[0, 0, 0]]
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solutions:
    def using_backtrack(self, n: int) -> List[Optional[int]]:
        def backtrack(n: int) -> List[Optional[int]]:
            if n == 0:
                return []
            if n == 1:
                return [ TreeNode() ]
            
            possible_trees = []
            for left_sub_tree in range(n):
                right_sub_tree = (n - 1) - left_sub_tree

                left = backtrack(left_sub_tree)
                right = backtrack(right_sub_tree)

                for tree1 in left:
                    for tree2 in right:
                        possible_trees.append(TreeNode(0, tree1, tree2))
            return possible_trees
        return backtrack(n)


    def using_cache(self, n: int) -> List[Optional[int]]:
        cache = { 0: [], 1: [ TreeNode() ] }

        def backtrack(n: int) -> List[Optional[int]]:
            if n % 2 == 0:
                return []
            
            if n in cache:
                return cache[n]

            possible_trees = []
            for left_sub_tree in range(n):
                right_sub_tree = (n - 1) - left_sub_tree

                left = backtrack(left_sub_tree)
                right = backtrack(right_sub_tree)

                for tree1 in left:
                    for tree2 in right:
                        possible_trees.append(TreeNode(0, tree1, tree2))
                
                cache[n] = possible_trees
            return possible_trees
        return backtrack(n)


    def using_cache_2(self, n: int) -> List[Optional[int]]:
        cache = { 0: [], 1: [ TreeNode() ]}
        
        def backtrack(n: int) -> List[Optional[TreeNode]]:
            if n % 2 == 0:
                return []
            
            if n not in cache.keys():
                possible_trees = []
                
                for left_sub_tree in range(n):
                    right_sub_tree = (n - 1) - left_sub_tree
                    
                    for left in backtrack(left_sub_tree):
                        for right in backtrack(right_sub_tree):
                            node = TreeNode(0)
                            node.left = left
                            node.right = right
                        
                            possible_trees.append(node)
                cache[n] = possible_trees
            return cache[n]
        return backtrack(n)