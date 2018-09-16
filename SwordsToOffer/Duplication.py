# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Duplication.py
time: 2018/9/8 22:27
"""
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        i = 0
        while(i < len(numbers)):
            if numbers[i] != i:
                temp = numbers[numbers[i]]
                numbers[numbers[i]] = numbers[i]
                numbers[i] = temp
            else:
                i += 1


