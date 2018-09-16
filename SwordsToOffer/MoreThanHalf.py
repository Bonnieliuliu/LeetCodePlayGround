# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MoreThanHalf.py
time: 2018/8/31 1:33
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 对列表进行快排
        if not numbers:
            return 0
        left = 0
        right = len(numbers) - 1
        middle = int((left+right+1)/2)
        while(True):
            index = self.Partition(left, right, numbers)
            if index < middle:
                left = index
            elif index >= middle:
                break
        if self.CheckNumber(numbers, middle):
            return numbers[middle]
        else:
            return 0
    def Partition(self, l, r, arr):

        x = arr[r]
        index= l-1
        for i in range(l, r):
            if  arr[i]<=x:
                index += 1
                arr[index], arr[i] = arr[i], arr[index]
        arr[index+1], arr[r] = arr[r], arr[index+1]
        print(arr, index+1)
        return index + 1
    def CheckNumber(self, arr, index):
        count = 0
        n = len(arr)
        t = arr[index]
        for number in arr:
            if number == t:
                count += 1
        if count > int(n/2):
            return True
        else:
            return False


def main():
    numbers = [1,2,3,2,2,2,5,4,2]
    s = Solution()
    res = s.MoreThanHalfNum_Solution(numbers)
    print(res)

if __name__ == "__main__":
    main()