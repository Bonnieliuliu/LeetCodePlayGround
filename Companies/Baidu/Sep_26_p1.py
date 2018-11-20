# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_26_p1.py
time: 2018/9/26 20:41
"""
class Solution(object):
    def Main(self, tinput):
        normal, treasure = 0, 0
        for line in tinput:
            index = line[0]
            if line[1] == 2:
                treasure += 1
            else:
                continue
        return normal, treasure



def main():
    n = int(input().strip())
    tinput = []
    for i in range(n):
        line = input().strip().split()
        line = [int(ele) for ele in line]
        line.insert(0, i+1)
        tinput.append(line)
    s = Solution()
    normal, treasure = s.Main(tinput)
    print(normal, treasure)

if __name__ == "__main__":
    main()