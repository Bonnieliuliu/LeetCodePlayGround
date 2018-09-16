# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: printMatrix.py
time: 2018/8/30 13:30
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        if matrix == []:
            return matrix
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return res
    def turn(self, matrix):
        numr = len(matrix)
        numc = len(matrix[0])
        new = []
        for j in range(numc-1, -1, -1):
            newrow = []
            for i in range(numr):
                newrow.append(matrix[i][j])
            new.append(newrow)
        return new

def main():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    s = Solution()
    res = s.printMatrix(matrix)
    print(res)

if __name__ == "__main__":
    main()