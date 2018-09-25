# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_25_p1.py
time: 2018/9/25 19:42
"""
class Solution(object):
    def Count(self, A):
        result = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    result += 1
                    A = self.helper(A, i, j)
        return result

    def helper(self, A, i, j):
        A[i][j] = 1
        while (i - 1 >= 0 and A[i - 1][j] == 0):
            A[i-1][j] = 1 - A[i-1][j]
            A = self.helper(A, i - 1, j)
        while (i + 1 < len(A) and A[i + 1][j] == 0):
            A[i+1][j] = 1- A[i+1][j]
            A = self.helper(A, i + 1, j)
        while (j - 1 >= 0 and A[i][j - 1] == 0):
            A[i][j-1] = 1-A[i][j-1]
            A = self.helper(A, i, j - 1)
        while (j + 1 < len(A[0]) and A[i][j + 1] == 0):
            A[i ][j+1] = 1- A[i][j+1]
            A = self.helper(A, i, j + 1)
        return A

def main():
    matrix = []
    for i in range(3):
        row = input().strip().split()
        new_row = []
        for ele in row:
            new_row.append(int(ele))
        matrix.append(new_row)
    s = Solution()
    result = s.Count(matrix)
    print(result)

if __name__ == "__main__":
    main()