# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: CanPlaceFlowers.py
time: 2018/7/15 12:37
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return True
        length = len(flowerbed)
        if length == 1:
            if n == 0:
                return True
            if n == 1:
                return flowerbed[0] == 0
        for i in range(length):
            if flowerbed[i] == 1:
                continue
            else:
                if i>=1 and i < length-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                elif i == 0 and flowerbed[i+1] == 0 and flowerbed[0] == 0:
                    n -= 1
                    flowerbed[i] = 1
                elif i == length - 1  and flowerbed[i-1] == 0 and flowerbed[length-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                else:
                    continue
            if n <= 0:
                return True
        return False

if __name__ == "__main__":
    input = [1, 0, 0, 0, 1]
    s = Solution()
    res = s.canPlaceFlowers(input, 1)
    print(res)