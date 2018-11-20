# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: KthLargestElementInTheArray.py
time: 2018/8/8 2:15
"""
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(True):
            index = self.partition(nums, left, right)
            if index == k-1:
                return nums[index]
            elif index > k-1:
                right = index - 1
            else:
                left = index + 1
    def partition(self, nums, left, right):
        i = left - 1
        pivot = nums[right]
        for j in range(left, right + 1):
            if nums[j] >= pivot:
                i += 1
                nums[i],nums[j]=nums[j],nums[i]
            else:
                continue
        return i
def main():
    input = [3,2,1,5,6,4]
    k = 2
    s = Solution()
    res = s.findKthLargest(input, k)
    print(res)

if __name__ == "__main__":
    main()