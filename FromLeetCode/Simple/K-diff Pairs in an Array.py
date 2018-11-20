# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: K-diff Pairs in an Array.py
time: 2018/7/29 23:28
"""
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        map_dict = {}
        for ele in nums:
            if ele not in map_dict:
                map_dict[ele] = 0
            map_dict[ele] += 1
        count = 0
        if k == 0:
            for key, value in map_dict.items():
                if value >= 2:
                    count += 1
            return count
        for key, value in map_dict.items():
            if key + k in map_dict:
                count += 1
        return count
