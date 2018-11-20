# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

4
1 0 0 0
0 0 0 0
0 0 0 1
0 0 0 0

5
1 0 0 1 1
1 0 0 1 1
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0

file: Sep_09_2.py
time: 2018/9/9 10:12
"""


class Solution(object):
    def GetNumberofConnected(self, m):
        numr = len(m)
        numc = len(m[0])
        result = 0
        for i in range(numr):
            for j in range(numc):
                if m[i][j] == 1:
                    result += 1
                    m = self.ChangeConnected(m, i, j)
        return result

    def ChangeConnected(self, m, i, j):
        numr = len(m)
        numc = len(m[0])
        m[i][j] = 0
        while (i - 1 >= 0 and m[i - 1][j] == 1):
            m = self.ChangeConnected(m, i - 1, j)
        while (i + 1 < numr and m[i + 1][j] == 1):
            m = self.ChangeConnected(m, i + 1, j)
        while (j - 1 >= 0 and m[i][j - 1] == 1):
            m = self.ChangeConnected(m, i, j - 1)
        while (j + 1 < numc and m[i][j + 1] == 1):
            m = self.ChangeConnected(m, i, j + 1)
        return m

import sys
def main():
    s = Solution()
    numr = int(sys.stdin.readline().strip())
    m = []
    for i in range(numr):
        line =sys.stdin.readline().strip()
        line = map(int, line.split())
        m.append(line)
    res = s.GetNumberofConnected(m)
    print(res)

if __name__ == '__main__':
    main()

