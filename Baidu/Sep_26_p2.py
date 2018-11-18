# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_26_p2.py
time: 2018/9/26 20:24
"""
import sys
class Solution(object):
    def Main(self, tinput):
        min_count = sys.maxsize
        index = 0
        for i in range(len(tinput)):
            temp = tinput[i]
            tinput[i] = 0
            _, count = self.Inversion(tinput)
            if count < min_count:
                index = i + 1
                min_count = count
            tinput[i] = temp
        return min_count, index

    def Inversion(self, arr):
        if len(arr) == 1:
            return arr, 0
        else:
            n = int(len(arr)/2)
            lst1, count1 = self.Inversion(arr[0:n])
            lst2, count2 = self.Inversion(arr[n:len(arr)])
            arr, count = self.Count(lst1, lst2, 0)
            return arr, count1 + count2 + count

    def Count(self, arr1, arr2, count):
        i = 0
        j = 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                count += len(arr1) - i
                j += 1
        res += arr1[i:]
        res += arr2[j:]
        return res, count


def main():
    n = input().strip().split()
    tinput = input().strip().split()
    tinput = [int(ele) for ele in tinput]
    s = Solution()
    count, index = s.Main(tinput)
    print(count, index)

if __name__ == "__main__":
    main()
