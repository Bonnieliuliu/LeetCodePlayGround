# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: 1.py
time: 2018/8/14 20:54
"""
import sys


class Solution():
    def dpPath(self, n, m, map):
        last_choice = [list(a) for a in map]
        best = [list(a) for a in map]
        for step in range(m - 1):
            for i in range(n):
                for j in range(n):
                    cost = []
                    for x in range(n):
                        if map[x][j] != 0 and last_choice[i][x] != 0:
                            cost.append(last_choice[i][x] + map[x][j])
                    local_best = min(cost)
                    best[i][j] = local_best
            last_choice = [list(x) for x in best]
        return best


def main():
    n = int(raw_input())
    m = int(raw_input())
    x = raw_input().split()
    map = []
    for i in range(n):
        map.append([int(x) for x in raw_input().split()])
    s = Solution()
    res = s.dpPath(n, m, map)
    for r in res:
        output = ""
        for ele in r:
            output = output + str(ele) +" "
        print(output)


if __name__ == "__main__":
    main()


