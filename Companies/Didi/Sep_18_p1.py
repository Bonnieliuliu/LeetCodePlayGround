# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_18_p1.py
time: 2018/9/18 20:00
"""
class Solution(object):
    def Balls(self, a, b, c, flag):
        if a<0 or b<0 or c<0:
            return 0
        if (a==1 and b==0 and c==0 and flag==0) or\
           (a==0 and b==1 and c==0 and flag==1) or\
           (a==0 and b==0 and c==1 and flag==2):
            return 1
        if flag==0:
            return self.Balls(a-1, b, c, 1)+self.Balls(a-1, b, c, 2)
        if flag==1:
            return self.Balls(a, b-1, c, 0)+self.Balls(a, b-1, c, 2)
        if flag==2:
            return self.Balls(a, b, c-1, 0)+self.Balls(a, b, c-1, 1)

def main():
    balls = (input().strip().split())
    a = int(balls[0])
    b = int(balls[1])
    c = int(balls[2])
    s = Solution()
    res = 0
    for flag in range(3):
        res += s.Balls(a, b, c, flag)
    print(res)

if __name__ == "__main__":
    main()