# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_16_p1.py
time: 2018/9/16 15:26
"""
import re
class Solution(object):
    def findSubSeq(self, a, k):
        res = set()
        for i in range(len(a)-k+1):
            cur = ""
            for j in range(i, i+k):
                cur += a[j]
            # if cur not in res:
            res.add(cur)
        return res

    def findSubSeqNumber(self, cur, b):
        res = 0
        for ele in cur:
            ans = len(re.findall(r'(?={0})'.format(ele), b))
            print(ele, ans)
            res+=ans
        return res



def main():
    k = int(input().strip())
    a = str(input().strip())
    b = str(input().strip())
    s = Solution()
    cur = s.findSubSeq(a, k)
    res = s.findSubSeqNumber(cur, b)
    print(res)

if __name__ == "__main__":
    main()
