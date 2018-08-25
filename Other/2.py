# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: 2.py
time: 2018/8/25 10:08
"""
from scipy.special import comb, perm
import sys

def ValidNumber(n):
    if n == 1:
        return 10
    ans = comb(2 * n, n) - comb(2 * n, n - 1)
    return ans % 1000000007


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    res = ValidNumber(n)
    print(res)