# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ReverseWordsInStringIII.py
time: 2018/7/23 22:21
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        sentence = s.split(" ")
        for word in sentence:
            word = self.swap(word)
            output += word + " "
        output = output[:-1]
        return output

    def swap(self, word):
        output = ''
        m = len(word)
        for i in range(m):
            output += word[m - 1 - i]
        return output


