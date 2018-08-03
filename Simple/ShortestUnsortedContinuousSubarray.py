# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ShortestUnsortedContinuousSubarray.py
time: 2018/7/18 23:54
"""
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        sort_nums = sorted(nums)
        start = 0
        end = -1
        n = len(nums)
        for i in range(n):
            if sort_nums[i] != nums[i]:
                start = i
                break
            else:
                continue
        for i in range(n):
            if nums[n-i-1] != sort_nums[n-i-1]:
                end = n - i - 1
                break
            else:
                continue
        res = end - start + 1
        return res
if __name__ == "__main__":
    s = Solution()
    input = [1,2,3,4]
    res = s.findUnsortedSubarray(input)
    assert res == 0
    print(res)