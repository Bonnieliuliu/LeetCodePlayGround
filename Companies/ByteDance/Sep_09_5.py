# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_09_5.py
time: 2018/9/9 11:57
"""
class Solution(object):
    def Sum(self, data):
        return 1
import sys
def main():
    s = Solution()
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    data =sys.stdin.readline().strip()
    data = map(int, data.split())
    res = s.Sum(data)
    print(res)

if __name__ == '__main__':
    # main()
    import re
    m = re.search('[0-9]','a1b2c3d4')
    print(m.group(0))