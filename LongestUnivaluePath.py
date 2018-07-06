# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: LongestUnivaluePath.py
time: 2018/7/6 12:53
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        _, res = self.Path(root, 0)
        return res

    def Path(self, son, res):
        if not son:
            return 0
        if son.left:
            left, res = self.Path(son.left, res)
        if son.right:
            right, res = self.Path(son.right, res)
        if son.left and son.val == son.left.val:
            left = left + 1
        else:
            left = 0
        if son.right and son.val == son.right.val:
            right = right + 1
        else:
            right = 0
        res = max(left + right, res)
        return max(left, right), res

