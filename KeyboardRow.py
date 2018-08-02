# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: KeyboardRow.py
time: 2018/8/1 1:58
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set()
        set1.update("qwertyuiop")
        set2 = set()
        set2.update("asdfghjkl")
        set3 = set()
        set3.update("zxcvbnm")
        output = []
        for word in words:
            one = 0
            two = 0
            three = 0
            for char in word:
                if char in set1:
                    one = 1
                if char in set2:
                    two = 1
                if char in set3:
                    three = 1
            if one+two+three == 1:
                output.append(word)
        return output

