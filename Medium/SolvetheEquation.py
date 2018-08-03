# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: SolvetheEquation.py
time: 2018/8/3 23:47
"""
class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left = equation.split("=")[0]
        right = equation.split("=")[1]
        left_c, left_x = self.process(left)
        right_c, right_x = self.process(right)
        left_x -= right_x
        right_c -= left_c
        if left_x == 0 and right_c == 0:
            return "Infinite solutions"
        if left_x == 0:
            return "No solutions"
        else:
            return "x=" + str(int(right_c / left_x))

    def process(self, part):
        if part[0] == "-":
            part = "0" + part
        part = part.replace("-", "+-")
        part = part.split("+")
        part_c, part_x = 0, 0
        for ele in part:
            if "x" in ele:
                if ele == "x":
                    part_x += 1
                elif ele == "-x":
                    part_x -= 1
                else:
                    part_x += int(ele[:-1])
            else:
                part_c += int(ele)
        return part_c, part_x

def main():
    input = "x=x+2"
    s = Solution()
    res = s.solveEquation(input)
    print(res)
if __name__ == "__main__":
    main()