# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PostOrder.py
time: 2018/7/17 1:51
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        s = []
        output = []
        s.append(root);
        while s:
            node = s[-1]
            s.pop();
            output.append(node.val)
            for child in node.children:
                s.append(child)
        output = output[::-1]
        return output
