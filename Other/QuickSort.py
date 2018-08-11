# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: QuickSort.py
time: 2018/8/4 11:15
"""
class Solution():
    def quicksort(self, nums):
        if len(nums)<=1:
            return nums
        l = 0
        r = len(nums)
        m = self.partition(nums, l, r)
        left = self.quicksort(nums[l:m])
        right = self.quicksort(nums[m+1: r])
        return left+[nums[m]]+right

    def partition(self, nums, l, r):
        i = l-1
        x = nums[r-1]
        for j in range(l, r):
            if nums[j] <= x:
                i+=1
                nums[i], nums[j]=nums[j], nums[i]
        return i


def main():
    input = [9,8,7,6,5,4,3,3,2,1]
    s = Solution()
    res = s.quicksort(input)
    print(res)

if __name__ == "__main__":
    main()