# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: IsSubsequence.py
time: 2018/8/19 21:51
"""


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True
        if len(t) <= 0:
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s) and s[i - 1] == t[j - 1]:
            return True
        else:
            return False

