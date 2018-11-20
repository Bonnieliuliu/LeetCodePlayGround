"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = ReverseString.py
time = 2018/8/11 22:24
more information
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        output = ""
        n = len(s)
        for i in range(n):
            output = output + s[n - 1 - i]
        return output
