# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: LongestHarmoniousSubsequence.py
time: 2018/7/16 21:30
"""
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}
        max_count = 0
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        for num, count in num_count.items():
            plus = 0
            minus = 0
            if num - 1 in num_count:
                minus = num_count[num] + num_count[num - 1]
            if num + 1 in num_count:
                plus = num_count[num] + num_count[num + 1]
            max_count = max(max_count, minus, plus)
        return max_count

if __name__ == "__main__":
    s = Solution()
    input = [1,1,1,1]
    res = s.findLHS(input)
    assert res == 0