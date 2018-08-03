# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ConstructStrFromBinaryTree.py
time: 2018/7/15 12:03
"""
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        output = ''
        output = self.RecursiveTree2Str(t, output)
        return output
    def RecursiveTree2Str(self, node, output):
        output += str(node.val)
        if node.left:
            output += '('
            output = self.RecursiveTree2Str(node.left, output)
            output += ')'
        elif not node.left and node.right:
             output += '()'
        if node.right:
            output += '('
            output = self.RecursiveTree2Str(node.right, output)
            output += ')'
        return output
