# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: RelativeRanking.py
time: 2018/7/31 23:30
"""
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        sorted_nums = sorted(nums, reverse=True)
        output = []
        rank_map = dict()
        i = 1
        for ele in sorted_nums:
            if i == 1:
                rank_map[ele] = "Gold Medal"
            elif i == 2:
                rank_map[ele] = "Silver Medal"
            elif i == 3:
                rank_map[ele] = "Bronze Medal"
            else:
                rank_map[ele] = str(i)
            i += 1
        for ele in nums:
            output.append(rank_map[ele])
        return output

def main():
    input = [10,3,8,9,4]
    s = Solution()
    res = s.findRelativeRanks(input)
    print(res)
if __name__ == "__main__":
    main()