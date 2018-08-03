# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: DetectCapital.py
time: 2018/7/30 0:50
"""
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        original = word
        if word.upper() == original:
            return True
        elif word[0].upper() == original[0] and word[1:].lower() == original[1:]:
            return True
        elif word.lower() == original:
            return True
        else:
            return False