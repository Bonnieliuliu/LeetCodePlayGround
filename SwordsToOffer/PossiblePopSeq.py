# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PossiblePopSeq.py
time: 2018/8/30 14:03
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return True
        if not pushV or not popV:
            return False
        j = 0
        stack = []
        print(pushV, popV)
        while j<len(popV):
            if stack and popV[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                if pushV:
                    ele = pushV.pop(0)
                    stack.append(ele)
                else:
                    break
        return len(stack) == 0

def main():
    push = [1,2,3,4,5]
    pop = [4,5,3,2,1]
    # push = [1, 2, 3, 4, 5]
    # pop = [3, 5, 4, 2, 1]
    s = Solution()
    print(push, pop)
    res = s.IsPopOrder(push, pop)
    print(res)

if __name__== "__main__":
    main()