# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: BaseBallGame.py
time: 2018/7/7 14:57
"""

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        for op in ops:
            if op == "D":
                score.append(score[-1] * 2)
            elif op == "C":
                score.pop()
            elif op == "+":
                score.append(score[len(score)-1] + score[len(score)-2])
            else:
                score.append(int(op))
        score_sum = sum(score)
        return score_sum



if __name__ == "__main__":
    s = Solution()
    raw_list = ["5","2","C","D","+"]
    res = s.calPoints(raw_list)
    print(res)
    assert res == 30