# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: sort.py
time: 2018/9/5 23:24
"""


class Solution(object):
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        l = 0
        r = len(arr) - 1
        index = self.Partition(l, r, arr)
        left = self.quickSort(arr[l:index])
        right = self.quickSort(arr[index+1:r+1])
        return left + [arr[index]] + right

    def Partition(self, l, r, arr):
        if l == r:
            return l
        index = l - 1
        x = arr[r]
        for i in range(l, r):
            if arr[i] <= x:
                index += 1
                arr[i], arr[index] = arr[index], arr[i]
        arr[r], arr[index + 1] = arr[index + 1], arr[r]
        return index + 1

    def MergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        middle = int((len(arr))/2)
        leftarr = self.MergeSort(arr[:middle])
        rightarr = self.MergeSort(arr[middle:])
        res = self.Merge(leftarr, rightarr)
        return res
    def Merge(self, left, right):
        res = []
        i = 0
        j = 0
        while(i<len(left) and j<len(right)):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i == len(left):
            for ele in right[j:]:
                res.append(ele)
        if j == len(right):
            for ele in left[i:]:
                res.append(ele)
        return res

def main():
    arr = [9,8,7,6,5,4,3,2,1]
    s = Solution()
    res = s.quickSort(arr)
    print(res)
    res = s.MergeSort(arr)
    print(res)

if __name__ == "__main__":
    main()