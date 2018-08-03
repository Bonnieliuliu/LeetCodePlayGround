# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: FindPeak.py
time: 2018/8/2 1:51
"""
class Solution:
    def findPeak(self, nums):
        """

        :param nums: List[int]
        :return: index of peak or -1: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums)
        m = (l+r) // 2
        if nums[m] > nums[m-1]:
            index = self.Recursive(nums, m, r)
        else:
            index = self.Recursive(nums, l, m)
        if index == r-1:
            # 一直增大，没有峰值
            return -1
        return index

    def Recursive(self, nums, left, right):
        if left == right - 1:
            return left
        m = (left+right)//2
        if nums[m] > nums[m-1]:
            index = self.Recursive(nums, m, right)
        else:
            index = self.Recursive(nums, left, m)
        return index

if __name__ == "__main__":
    s = Solution()
    input = [1, 2, 1]
    res = s.findPeak(input)
    print(res)