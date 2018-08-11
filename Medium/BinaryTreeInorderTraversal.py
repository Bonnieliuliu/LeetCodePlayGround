# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: BinaryTreeInorderTraversal.py
time: 2018/8/6 1:28
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        parent = [root]
        output = []
        final = []
        while parent:
            node = parent[-1]
            while node.left and node.left not in output:
                parent.append(node.left)
                node = node.left
            parent.pop()
            output.append(node)
            if node.right:
                parent.append(node.right)
        for item in output:
            final.append(item.val)
        return final