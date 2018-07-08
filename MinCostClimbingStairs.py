# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MinCostClimbingStairs.py
time: 2018/7/8 15:32
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return cost[1]
        min_cost = [None]*len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2, len(cost)):
            min_cost[i] = min(min_cost[i-1]+cost[i], min_cost[i-2]+cost[i])
        print(min_cost)
        minimum = min(min_cost[len(cost)-1], min_cost[len(cost)-2])
        return minimum

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s = Solution()
    res = s.minCostClimbingStairs(cost)
    print(res)
