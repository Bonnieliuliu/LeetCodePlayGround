# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_08_1.py
time: 2018/9/8 15:52
"""

class Solution():
    def FindMaxLength(self, tinput):
        if not tinput:
            return 0
        if len(tinput) == 1:
            return 1
        if len(tinput) == 2:
            if tinput[0] == tinput[1]:
                return 2
            else:
                return 1
        if(tinput[0]==tinput[-1]):
            tinput = self.turn(tinput)
        res = 0
        color = tinput[0]
        cur = 1
        for i in range(1, len(tinput)):
            if color == tinput[i]:
                cur += 1
            else:
                cur = 1
            if cur > res:
                res = cur
            color = tinput[i]
        return res
    def turn(self, tinput):
        color = tinput[0]
        for i in range(1, len(tinput)):
            if tinput[i] == color:
                continue
            else:
                break
        last = i-1
        t1 = tinput[:last+1]
        t1 = t1[::-1]
        t3 = tinput[last+1:]
        t3 = t3[::-1]
        output = t1+t3
        return output

def main():
    tinput = str(input())
    s = Solution()
    res = s.FindMaxLength(tinput)
    print(res)

if __name__ == "__main__":
    main()