# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Base7.py
time: 2018/7/31 23:43
"""
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return '-' + self.convertToBase7(-num)
        if num == 0:
            return '0'
        output = ''
        while num != 0:
            output = str(num % 7) + output
            print(num%7)
            num //= 7
        return output

def main():
    input = -7
    s = Solution()
    res = s.convertToBase7(input)
    print(res)

if __name__ == "__main__":
    main()