# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: GetLeastKNumbers.py
time: 2018/9/2 16:02
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        if k <=0 or k > len(tinput):
            return []
        l = 0
        r = len(tinput) - 1
        index = self.Partition(l, r, tinput)
        while (index != k-1):
            if index > k-1:
                r = index-1
                index = self.Partition(l, r, tinput)
            else:
                l = index+1
                index = self.Partition(l, r, tinput)
        res = tinput [:k]
        print(tinput)
        res.sort()
        return res
    def Partition(self, l, r, arr):
        print(arr)
        x = arr[r]
        index = l - 1
        for i in range(l, r):
            if arr[i] <= x:
                index += 1
                arr[i], arr[index] = arr[index], arr[i]
        arr[index + 1], arr[r] = arr[r], arr[index + 1]
        return index + 1

def main():
    tinput = [5,4,3,2,1,10,9,8,7,6]
    k = 4
    s = Solution()
    res = s.GetLeastNumbers_Solution(tinput, k)
    print(res)

if __name__ == "__main__":
    main()