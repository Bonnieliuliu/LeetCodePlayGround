# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_20_p3.py
time: 2018/9/20 19:49
"""
class Solution(object):
    def FindWord(self, tinput, matrix):
        if not tinput:
            return None
        visited = list()
        result = []
        for word in tinput:
            if self.StartFromFirst(visited, matrix, word):
                result.append(word)
        return result

    def StartFromFirst(self, visited, matrix, word):
        cur_char = word[0]
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == cur_char:
                    visited.append([i, j])
                    flag = self.FindNextWordInMatrix(visited, matrix, word[1:], i, j)
                    if flag:
                        return True
                    else:
                        visited.remove([i, j])
        return False

    def FindNextWordInMatrix(self, visited, matrix, word, i, j):
        if not word:
            return True
        row = len(matrix)
        column = len(matrix[0])
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        curchar = word[0]
        for direc in directions:
            # check boundaries
            if i + direc[0]>=0 and i+direc[0]<=row-1 and j +direc[1]>=0 and j+direc[1]<=column-1:
                # check equality
                if matrix[i+direc[0]][j+direc[1]] == curchar:
                    visited.append([i+direc[0], j+direc[1]])
                    flag = self.FindNextWordInMatrix(visited, matrix, word[1:], i+direc[0], j+direc[1])
                    if flag:
                        return True
                    else:
                        visited.remove([i+direc[0], j+direc[1]])

        return False


def main():
    num_list = input().strip().split()
    n = int(num_list[1])
    tinput = input().strip().split()
    word_matrix = []
    for i in range(n):
        row = input().strip().split()
        word_matrix.append(row)
    s = Solution()
    result = s.FindWord(tinput, word_matrix)
    for answer in result:
        print(answer)

if __name__ == "__main__":
    main()