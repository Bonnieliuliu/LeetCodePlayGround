# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: 4.py
time: 2018/8/25 11:15
"""


def LongestSubSeq(n, m, arr):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = []
    for i in range(m):
        nums.extend(arr)
    N = len(nums)
    dp = [0] * N
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] += 1
    return max(dp)

import sys
if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    num = list(map(int, line.split()))
    n = num[0]
    m = num[1]
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    arr = list(map(int, line.split()))
    res = LongestSubSeq(n, m, arr)
    print(res)
