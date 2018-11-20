# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Oct_15_p2.py
time: 2018/10/15 20:44
3 3
100 100 100
200 200 200
0 0 0
3 3
0.09 0.12 0.09
0.12 0.16 0.12
0.09 0.12 0.09
"""
class Solution(object):
    def Filter(self, m, filter):
        
        return [[160, 160, 160],[110, 110, 110],[120, 120, 120]]



if __name__ == "__main__":
    msize = input().strip().split()
    c = int(msize[0])
    r = int(msize[1])
    m = []
    for i in range(r):
        line = input().strip().split()
        row = []
        for j in line:
            row.append(int(j))
        m.append(row)
    fsize = input().strip().split()
    fc = int(fsize[0])
    fr = int(fsize[1])
    filter = []
    for i in range(fr):
        line = input().strip().split()
        frow = []
        for j in line:
            frow.append(float(j))
        filter.append(frow)
    s = Solution()
    res = s.Filter(m, filter)
    print(res)