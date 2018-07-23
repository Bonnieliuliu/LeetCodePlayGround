# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: diameterOfBinaryTree.py
time: 2018/7/24 2:25
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = 0
        right_depth = 0
        res = self.depth(root.left, left_depth) + self.depth(root.right, right_depth)
        res = max(res, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return res

    def depth(self, node, depth):
        if not node:
            return depth
        depth += 1
        depth = max(self.depth(node.left, depth), self.depth(node.right, depth))
        return depth