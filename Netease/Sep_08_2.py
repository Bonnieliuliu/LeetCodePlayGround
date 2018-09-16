# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn
6
1 0
1 1
2 0
2 1
2 2
6 2
file: Sep_08_2.py
time: 2018/9/8 15:59
"""
class Solution():
    def MaxMinLiving(self, n, k):

        if n<=2 or k>=n or k<=1:
            return 0, 0
        if 2*k-1<=n:
            mini = 0
            maxi = k - 1

        else:
            mini = 0
            maxi = n - k
        return mini, maxi
def main():
    t = int(input())
    s = Solution()
    res = []
    for i in range(t):
        line = input().strip().split(" ")
        line = list(map(int, line))
        ans = s.MaxMinLiving(line[0],line[1])
        res.append(ans)
    for ele in res:
        print(ele[0], ele[1])

if __name__ == "__main__":
    main()