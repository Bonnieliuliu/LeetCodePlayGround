# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Range Sum Query - Immutable.py
time: 2018/8/16 1:19
"""


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)