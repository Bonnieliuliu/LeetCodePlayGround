# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_09_1.py
time: 2018/9/9 10:01
"""
class Solution(object):
    def MaxLengthUnreapeted(self, s):
        if len(s) <= 0:
            return 0
        if len(s) == 1:
            return 1

        subseq = []
        n = len(s)
        for i in range(n):
            tmp = s[i]
            for j in range(i + 1, n):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    break
            subseq.append(tmp)
        subseq.sort(lambda x, y: cmp(len(x), len(y)))
        res = len(subseq[-1])
        return res

import sys
def main():
    s = Solution()
    tinput = sys.stdin.readline().strip()
    res = s.MaxLengthUnreapeted(tinput)
    print(res)

if __name__ == '__main__':
    main()