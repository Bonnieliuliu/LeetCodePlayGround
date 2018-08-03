# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MaximumLengthofPairChains.py
time: 2018/8/3 22:36
"""
from operator import itemgetter
import sys, json

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs.sort(key=itemgetter(1))
        stack = []
        stack.append(pairs[0])
        for pair in pairs:
            top = stack[-1]
            if top[1] < pair[0]:
                stack.append(pair)
        return len(stack)


def stringToIntList(nums):
    return json.loads(nums)

def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntList(line)
            s = Solution()
            res = s.findLongestChain(nums)
            print(res)
        except StopIteration:
            pass
if __name__ == "__main__":
    main()

