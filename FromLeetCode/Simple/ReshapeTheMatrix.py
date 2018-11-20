# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ReshapeTheMatrix.py
time: 2018/7/19 0:53
"""


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(0)
            res.append(row)
        for i in range(r):
            for j in range(c):
                k = (i * c + j) // n
                p = (i * c + j) % n
                res[i][j] = nums[k][p]
        return res

if __name__ == "__main__":
    nums = [[1,2],[3,4]]
    r = 1
    c = 4
    s = Solution()
    res = s.matrixReshape(nums, r, c)
    print(res)
    assert res == [[1,2,3,4]]