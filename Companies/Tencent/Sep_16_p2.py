# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_16_p2.py
time: 2018/9/16 15:55
"""
import math
class Solution(object):
    def MinimumRound(self, s1, s2):
        ssum = 2 * (s1 + s2)
        index = 0
        for i in range(int(math.sqrt(ssum))+1):
            if i * (i+1) == ssum:
                index = i
                break
        if index * (index+1) != ssum:
            return -1
        round = 1
        ss1 = s1
        while(ss1 > index):
            ss1 = ss1 - index
            index -= 1
            round+=1
        return round


def main():
    score = (input().strip().split())
    s1 = int(score[0])
    s2 = int(score[1])
    s = Solution()
    res = s.MinimumRound(s1, s2)
    print(res)

if __name__ == "__main__":
    main()