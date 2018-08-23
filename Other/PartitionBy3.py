# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PartitionBy3.py
time: 2018/8/23 23:18

题目：
一个数组，不用其他内存，让这个数组 % 3 = 0 的放最前面，% 3 = 1 的放中间，% 3 = 2 的放最后; O(N)搞定
"""

class Solution():
    def PartitionBy3(self, arr):
        """

        :param arr: list[int]
        :return: arr: list[int]
        """
        i = 0
        j = len(arr)-1
        index = 0
        while index < len(arr):
            print(arr)
            if arr[index] % 3 == 0:
                arr[i],arr[index] = arr[index], arr[i]
                i += 1
            else:
                index += 1
        index = j
        print("="*30)
        while index>=i:
            print(arr)
            if arr[index] % 3 == 2:
                arr[j],arr[index] = arr[index], arr[j]
                j -= 1
            else:
                index-=1
        return arr

def main():
    arr = [1,2,3,4,5,6,7,8,9]
    s = Solution()
    res = s.PartitionBy3(arr)
    print("Final Answer: {}".format(res))

if __name__ == "__main__":
    main()