# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_20_p1.py
time: 2018/9/20 19:04
"""
class Solution(object):
    def Simple(self, s):
        if not s:
            return ""
        s = s.split("/")
        if s[-1]!="":
            last = s[-1]
        else:
            last = s[-2]
        return "/"+last

def main():
    tinput = str(input().strip())
    s = Solution()
    res = s.Simple(tinput)
    print(res)

if __name__ == "__main__":
    main()