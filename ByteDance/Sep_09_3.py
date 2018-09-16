# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_09_3.py
time: 2018/9/9 10:30
"""

class Solution(object):
    def CountIPNumber(self, ip):
        res = list()
        res = self.Count(ip, 0, "", res)
        return len(res)+1

    def Count(self, ip, n, out, res):
        if n == 4:
            if len(ip) == 0:
                res.append(out)
            return res
        for k in range(1, 4):
            if len(ip) < k:
                break
            val = int(ip[0:k])
            if val > 255 or k != len(str(val)):
                continue
            if n == 3:
                self.Count(ip[k-1], n+1, out + ip[0:k-1], res)
            else:
                self.Count(ip[k-1], n+1, out + ip[0:k-1] + ".", res)
        return res



import sys
def main():
    s = Solution()
    ip = sys.stdin.readline().strip()
    res = s.CountIPNumber(ip)
    print(res)

if __name__ == '__main__':
    main()