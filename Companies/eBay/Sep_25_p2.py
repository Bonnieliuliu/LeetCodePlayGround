# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_25_p2.py
time: 2018/9/25 20:02
"""
class Solution(object):
    def TotalNum(self, n, t):
        arr = []
        for i in range(n):
            arr.append(i+1)
        res = self.perm(arr, 0, len(arr), t, 0)
        return res

    def perm(self, n, begin, end, t, res):
        global COUNT
        if begin >= end:
            count, _ = self.InversionNum(n)
            if count == t:
                res += 1
            COUNT += 1
        else:
            i = begin
            for num in range(begin, end):
                n[num], n[i] = n[i], n[num]
                n, res = self.perm(n, begin + 1, end, t, res)
                n[num], n[i] = n[i], n[num]
        return n, res

    def InversionNum(self, lst):
        if len(lst) == 1:
            return lst, 0
        else:
            n = len(lst) // 2
            count1, lst1 = self.InversionNum(lst[0:n])
            count2, lst2 = self.InversionNum(lst[n:len(lst)])
            lst, count = self.Count(lst1, lst2, 0)
            return count1 + count2 + count, lst

    def Count(self, lst1, lst2, count):
        i = 0
        j = 0
        res = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                count += len(lst1) - i
                j += 1
        res += lst1[i:]
        res += lst2[j:]
        return res, count


def main():
    tinput = input().strip().split()
    n = int(tinput[0])
    t = int(tinput[1])
    s = Solution()
    count, result = s.TotalNum(n, t)

if __name__ == "__main__":
    main()
