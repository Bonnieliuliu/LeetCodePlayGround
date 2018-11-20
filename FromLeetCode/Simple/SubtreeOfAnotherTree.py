# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: SubtreeOfAnotherTree.py
time: 2018/7/19 0:35
"""
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t and not s:
            return True
        if not s:
            return False
        if self.IsSame(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def IsSame(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return self.IsSame(s.left, t.left) and self.IsSame(s.right, t.right)
        else:
            return False