# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn
3
235 140 4
file: Sep_09_4.py
time: 2018/9/9 11:41
"""


class Solution(object):
    def Valid(self, data):
        cnt = 0
        for d in data:
            if cnt == 0:
                if (d >> 5) == 0b110:
                    cnt = 1
                elif (d >> 4) == 0b1110:
                    cnt = 2
                elif (d >> 3) == 0b11110:
                    cnt = 3
                elif d >> 7:
                    return False
                continue
            if (d >> 6) != 0b10:
                return False
            cnt -= 1
        return cnt == 0

import sys
def main():
    s = Solution()
    num = int(sys.stdin.readline())
    line = sys.stdin.readline().strip().split()
    line = map(int, line)
    res = s.Valid(line)
    if res:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
