# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: DiceStraightSmall.py
time: 2018/11/17 16:21
"""

class Solution():
    def helper(self):
        return

if __name__ == "__main__":
    s = Solution()
    with open("A-small-practice.in") as f:
        tests = int(f.readline())
    wf = open("A-small-practice.out", "w")
    for i in range(1, tests+1):
        wf.writelines("Case #{0}: {1}\n".format(i, i))
    wf.close()
