# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MaximumSubarray.py
time: 2018/7/13 1:31
"""
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        temp_sum = 0
        max_sum = 0
        left = 0
        for i in range(k):
            max_sum += nums[i]
            temp_sum += nums[i]
        for i in range(k, n):
            temp_sum = temp_sum + nums[i] - nums[left]
            if temp_sum > max_sum:
                max_sum = temp_sum
            left += 1
        return max_sum / k

if __name__ == "__main__":
    array = [2,-12,23,324,42,-222]
    s = Solution()
    res = s.findMaxAverage(array, 4)
    print(res)