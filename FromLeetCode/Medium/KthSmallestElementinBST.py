# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: KthSmallestElementinBST.py
time: 2018/8/6 0:41
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return k
        output = []
        output = self.inorder(root, output)
        for i in range(len(output)):
            if i == k-1:
                res = output[i].val
                break
        return res
    def inorder(self, node, output):
        if not node:
            return output
        output = self.inorder(node.left, output)
        output.append(node)
        output = self.inorder(node.right, output)
        return output