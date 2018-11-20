# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Climbing Stairs.py
time: 2018/8/16 1:17
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        count = 0
        frontfront = 1
        front = 2
        for i in range(3, n + 1):
            count = frontfront + front
            frontfront = front
            front = count
        return count
