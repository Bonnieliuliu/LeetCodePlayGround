# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn
4
9000
0
27000
18001
file: Sep_10_p2.py
time: 2018/9/10 18:51
"""
class Solution(object):
    def CountTriangle(self, data):
        n = len(data)
        res = 0
        i = 0
        while(i<n and data[i]<180):
            cnt = 0
            maxi = data[i]+180
            for j in range(i+1, n):
                if (data[j]<maxi):
                    cnt+=1
            res += int(cnt*(cnt-1)/2)
            i+=1
        while(i<n and data[i]>180):
            cnt = 0
            maxi = data[i]-180
            for j in range(i+1, n):
                if (data[j]>maxi):
                    cnt += 1
            res += int(cnt*(cnt-1)/2)
            i+=1
        return res

def main():
    n = int(input())
    tinput = []
    for i in range(n):
        tinput.append(int(input())/100)
    tinput.sort()
    print(tinput)
    s = Solution()
    res = s.CountTriangle(tinput)
    print(res)

if __name__== "__main__":
    main()
