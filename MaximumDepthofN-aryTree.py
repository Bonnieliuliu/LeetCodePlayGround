# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MaximumDepthofN-aryTree.py
time: 2018/7/22 17:56
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        level = 1
        max_level = level
        for child in root.children:
            cur_level =self.Depth(child, level)
            if cur_level > max_level:
                max_level = cur_level
        return max_level
    def Depth(self, node, level):
        if not node:
            return level
        level += 1
        max_level = level
        for child in node.children:
            cur_level = self.Depth(child, level)
            if cur_level > max_level:
                max_level = cur_level
        return max_level