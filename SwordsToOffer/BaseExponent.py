# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: BaseExponent.py
time: 2018/8/29 20:30
"""
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent < 0:
            return 1 / self.Power(base, -exponent)
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        res = self.Power(base, int(exponent/2))
        if (exponent % 2):
            return res*res*base
        else:
            return res*res

def main():
    arr = input().split()
    base = int(arr[0])
    exponent = int(arr[1])
    s = Solution()
    res = s.Power(base, exponent)
    print(res)

if __name__ == "__main__":
    main()