# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: setMisMatch.py
time: 2018/7/11 20:46
"""
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set()
        sum = 0
        res = []
        for num in nums:
            sum += num
            if num not in s:
                s.add(num)
            else:
                redudant = num
        missing = int(n*(n+1)/2) + redudant -sum
        return [redudant, missing]

if __name__ == "__main__":
    s= Solution()
    wrong_list = [1,2,2,4]
    res = s.findErrorNums(wrong_list)
    print("Redudant number is {0}\nMissing number is {1}".format(res[0], res[1]))