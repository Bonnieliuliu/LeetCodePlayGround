# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: JewelsandStones.py
time: 2018/8/4 12:45
"""


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jew_num = dict.fromkeys(J, 0)
        count = 0
        for stone in S:
            if stone in J:
                jew_num[stone] += 1
        for key, value in jew_num.items():
            count += value
        return count
