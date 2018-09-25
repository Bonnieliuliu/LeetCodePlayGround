# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_20_p5.py
time: 2018/9/20 20:26
"""
class Solution(object):
    def FindHappyNumber(self, left, right):
        num_happy = 0
        for data in range(left, right+1):
            digit_list = []
            for digit in str(data):
                digit = int(digit)
                digit_list.append(int(digit))
                continue
            while(len(digit_list)>1):
                first= digit_list[0]
                last = digit_list[-1]
                if first == last:
                    break
                else:
                    digit_list.pop(0)
                    digit_list.pop(-1)
            if len(digit_list) == 1 or len(digit_list) == 0:
                num_happy += 1
        return num_happy


def main():
    num_list = input().strip().split()
    left = int(num_list[0])
    right = int(num_list[1])
    s = Solution()
    result = s.FindHappyNumber(left, right)
    print(result)

if __name__ == "__main__":
    main()