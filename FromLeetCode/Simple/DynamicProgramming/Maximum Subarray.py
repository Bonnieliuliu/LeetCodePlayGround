# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Maximum Subarray.py
time: 2018/8/16 1:16
"""
import sys
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = - sys.maxsize
        maxcount = count
        for ele in nums:
            if count > 0:
                count += ele
            else:
                count = ele
            if maxcount < count:
                maxcount = count
        return maxcount