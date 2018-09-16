# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MaxSubSum.py
time: 2018/9/2 18:15
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxsum = len(array)*[0]
        maxsum[0] = array[0]
        for i in range(1, len(array)):
            if maxsum[i-1]<0:
                maxsum[i] = array[i]
            else:
                maxsum[i] = maxsum[i-1]+array[i]
        return max(maxsum)

def main():
    s = Solution()
    array = [6,-3,-2,7,-15,1,2,2]
    res = s.FindGreatestSumOfSubArray(array)
    print(res)

if __name__ == "__main__":
    main()