# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: RangeAdditionII.py
time: 2018/7/15 15:06
"""


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        x = m
        y = n
        for op in ops:
            x = min(x, op[0])
            y = min(y, op[1])
        return x * y

if __name__ == "__main__":
    s = Solution()
    m , n = 3, 3
    ops = [[2,2],[3,3]]
    res = s.maxCount(m,n,ops)
    assert res == 4