# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_10_p1.py
time: 2018/9/10 18:51
"""
class Solution(object):
    def LessSum(self, a):
        res = []
        for ele in a:
            cur = 0
            for less in a:
                if less<ele:
                   cur+=less
            res.append(cur)
        return res

def main():
    m = int(input())
    tinput= []
    if m == 0:
        print(0)
    else:
        for i in range(m):
            tinput.append(int(input()))
        s = Solution()
        res = s.LessSum(tinput)
        for ele in res:
            print(ele)

if __name__== "__main__":
    main()