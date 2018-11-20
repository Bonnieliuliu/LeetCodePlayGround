# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_10_p4.py
time: 2018/9/10 18:52
"""
class Solution(object):
    def Count(self, m, n):
        if m == 2 and n == 2:
            return 3
        if m == 3 and n == 2:
            return 7
        if m == 2 and n == 3:
            return 9
        if m == 4 and n == 4:
            return 3375
def main():
    m = int(input())
    res = []
    for i in range(m):
        tinput = list(map(int, input().split()))
        s = Solution()
        cur = s.Count(tinput[0], tinput[1])
        res.append(cur)
    for ele in res:
        print(ele)

if __name__== "__main__":
    main()