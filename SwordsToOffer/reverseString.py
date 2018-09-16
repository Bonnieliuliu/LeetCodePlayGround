# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: reverseString.py
time: 2018/9/6 8:56
"""

class Solution(object):
    def ReverseSentence(self, s):
        # write code here
        # return " ".join(s.split(" ")[::-1])
        res = ""
        lists = s.split(" ")
        while (lists):
            ele = lists.pop()
            res += ele + " "
        res.strip()
        return res

def main():
    s = Solution()
    input = "student a am I"
    res = s.ReverseSentence(input)
    print(res)

if __name__ == "__main__":
    main()
