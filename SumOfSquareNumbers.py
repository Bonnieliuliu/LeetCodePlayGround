# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: SumOfSquareNumbers.py
time: 2018/7/13 21:45
"""
from math import sqrt


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        sqr_c = int(sqrt(c))
        if sqr_c * sqr_c == c:
            return True
        else:
            for i in range(sqr_c + 1):
                remain = c - i * i
                sqr_remain = int(sqrt(remain))
                if sqr_remain * sqr_remain == remain:
                    return True
        return False

if __name__ == "__main__":
    input = 2
    s = Solution()
    res = s.judgeSquareSum(input)
    print(res)
    assert res == True