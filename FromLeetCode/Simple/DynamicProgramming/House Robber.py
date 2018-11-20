# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: House Robber.py
time: 2018/8/16 1:18
"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            rev = nums[0]
            return rev
        if len(nums) == 2:
            rev = max(nums)
            return rev
        n = len(nums)
        rev = []
        rev.append(nums[0])
        rev.append(max(nums[0], nums[1]))
        for i in range(2, n):
            cur = max(rev[i - 2] + nums[i], rev[i - 1])
            rev.append(cur)
        return rev[-1]
