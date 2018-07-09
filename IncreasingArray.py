# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: IncreasingArray.py
time: 2018/7/9 21:47
"""
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or nums == []:
            return True
        if len(nums) == 1:
            return True
        if len(nums) == 2:
            return True
        count = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                if count == 0:
                    if i >= 2:
                        if nums[i] >= nums[i-2]:
                            nums[i-1] = nums[i-2]
                        else:
                            nums[i] = nums[i-1]
                    else:
                        nums[i-1] = nums[i]
                    count += 1
                else:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    nums = [4,2,1]
    nums = [4,2,3]
    # nums = None
    res = s.checkPossibility(nums)
    print(res)