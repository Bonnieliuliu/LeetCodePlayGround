# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MaximumProdutOfThreeNumbers.py
time: 2018/7/13 23:19
"""


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        q = nums[n - 3] * nums[n - 2] * nums[n - 1]
        q = max(q, nums[0] * nums[1] * nums[n - 1])
        return q

if __name__ == "__main__":
    s = Solution()
    input = [1,2,3,4]
    res = s.maximumProduct(input)
    print(res)