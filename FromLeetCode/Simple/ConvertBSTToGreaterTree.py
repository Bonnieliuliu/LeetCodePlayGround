# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ConvertBSTToGreaterTree.py
time: 2018/7/29 23:26
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        summation = 0
        root, summation = self.AddSum(root, summation)
        return root

    def AddSum(self, node, summation):
        if not node:
            return node, summation
        node.right, summation = self.AddSum(node.right, summation)
        node.val += summation
        summation = node.val
        node.left, summation = self.AddSum(node.left, summation)
        return node, summation