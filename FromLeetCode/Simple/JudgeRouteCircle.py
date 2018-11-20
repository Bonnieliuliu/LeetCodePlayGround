# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: JudgeRouteCircle.py
time: 2018/7/10 20:02
"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        circle = {"L": 0, "R": 0, "U": 0, "D": 0}
        for move in moves:
            circle[move] += 1
        if circle["L"] == circle["R"] and circle["U"] == circle["D"]:
            return True
        else:
            return False
if __name__ == "__main__":
    moves = "UUUDDDLR"
    s = Solution()
    res = s.judgeCircle(moves)
    print(res)
    assert res == True