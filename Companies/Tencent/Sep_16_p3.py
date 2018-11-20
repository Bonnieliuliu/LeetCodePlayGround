# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_16_p3.py
time: 2018/9/16 16:12
"""
import math
class Solution(object):
    def TriangleNumber(self, a, b, c):
        num = 0
        for i in range(1, a+1):
            for j in range(1, b+1):
                for k in range(1, c+1):
                    if self.helper(i, j, k):
                        num += 1
        num = int(num/2)
        return num % 1000000007
    def helper(self, i, j, k):
        if i <=0 or j <=0 or k<=0:
            return False
        res = [i, j, k]
        res.sort()
        mini = res[0]
        maxi = res[1]
        if res[1] > maxi-mini and mini> maxi-res[1] and maxi> res[1]-mini \
                and maxi < res[1]+res[0]:
            return True
        return False

def main():
    triangle = (input().strip().split())
    a = int(triangle[0])
    b = int(triangle[1])
    c = int(triangle[2])
    s = Solution()
    res = s.TriangleNumber(a, b, c)
    print(res)

if __name__ == "__main__":
    main()