# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: DistributeCandies.py
time: 2018/7/18 23:59
"""


class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies) == 0:
            return 0
        candy_set = set()
        for candy in candies:
            if candy not in candy_set:
                candy_set.add(candy)
        res = min(len(candy_set), int(len(candies) / 2))
        return res

if __name__ == "__main__":
    s = Solution()
    input = [1,2,1,2,3,3]
    res = s.distributeCandies(input)
    assert res == 3
    print(res)