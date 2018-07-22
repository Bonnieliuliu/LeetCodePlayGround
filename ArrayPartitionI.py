# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ArrayPartitionI.py
time: 2018/7/22 15:26
"""
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(0, len(nums) - 1, 2):
            res += nums[i]
        return res

if __name__ == "__main__":
    s = Solution()
    input = [1,4,2,3]
    res = s.arrayPairSum(input)
    assert res == 4
    print(res)