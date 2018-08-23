# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: IslandPerimeter.py
time: 2018/8/24 1:27
"""


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if (i == 0 or grid[i - 1][j] == 0):
                    res += 1
                if (i == len(grid) - 1 or grid[i + 1][j] == 0):
                    res += 1
                if (j == 0 or grid[i][j - 1] == 0):
                    res += 1
                if (j == len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    res += 1
        return res
