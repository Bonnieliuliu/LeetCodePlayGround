# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PictureSmoother.py
time: 2018/7/10 19:53
"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return
        m = len(M)
        n = len(M[0])
        res = []
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, -1], [1, 1], [-1, 1], [-1, -1]]
        for i in range(m):
            row = []
            for j in range(n):
                count = 1
                sum_sur = M[i][j]
                for dir in dirs:
                    if (i + dir[0] < 0 or i + dir[0] >= m or j + dir[1] < 0 or j + dir[1] >= n):
                        continue
                    count += 1
                    sum_sur += M[i + dir[0]][j + dir[1]]
                row.append(int(sum_sur / count))
            res.append(row)
        return res
if __name__ == "__main__":
    M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    s = Solution()
    res = s.imageSmoother(M)
    print(res)