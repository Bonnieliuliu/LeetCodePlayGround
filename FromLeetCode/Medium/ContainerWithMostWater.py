"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = ContainerWithMostWater.py
time = 2018/8/11 23:15
more information
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height)-1
        while(left<right):
            maxArea = max(maxArea, min(height[left], height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea