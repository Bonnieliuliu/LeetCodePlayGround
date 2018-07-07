# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: findLengthOfLCIS.py
time: 2018/7/7 15:58
"""

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        max_len = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
        return max_len

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,4,2,3,4,5]
    res = s.findLengthOfLCIS(nums)
    print(res)