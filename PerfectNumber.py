# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PerfectNumber.py
time: 2018/7/30 1:00
"""
import math


import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return False
        summation = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                summation += int(num/i) +i
            if i*i == num:
                summation -= i
        return summation == num


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            num = int(line)

            ret = Solution().checkPerfectNumber(num)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()