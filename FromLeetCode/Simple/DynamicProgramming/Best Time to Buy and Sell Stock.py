# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Best Time to Buy and Sell Stock.py
time: 2018/8/16 1:18
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        if len(prices)<=1:
            return 0
        mini = prices[0]
        maxi = prices[0]
        biggest = -sys.maxsize
        for ele in prices:
            if ele > mini:
                if ele >maxi:
                    maxi = ele
                else:
                    continue
            else:
                mini = ele
                maxi = ele
            revenue = maxi - mini
            if revenue > biggest:
                biggest = revenue
        return biggest