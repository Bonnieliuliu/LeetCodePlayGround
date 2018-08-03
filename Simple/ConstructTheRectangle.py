# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ConstructTheRectangle.py
time: 2018/8/2 1:47
"""
import math,sys
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area < 0:
            return [None, None]
        if area == 0:
            return [0, 0]
        limit = int(math.sqrt(area))
        if limit * limit == area:
            return [limit, limit]
        sub = sys.maxsize
        print(sub)
        for width in range(1, limit+1):
            length = area // width
            if width*length == area:
                if length - width < sub:
                    output = [length, width]
                else:
                    continue
        return output

if __name__ == "__main__":
    s = Solution()
    input = 18
    res = s.constructRectangle(input)
    print(res)
