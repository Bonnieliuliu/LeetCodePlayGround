# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: ReverseWordsInStringIII.py
time: 2018/7/23 22:21
"""


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        list_s = list(s)
        t = ""
        if n <= k:
            list_s.reverse()
            return "".join(list_s)
        count = n // k
        for i in range(count+1):
            if i % 2 == 0:
                if i * k + k <= n:
                    list_s[i * k: i * k + k] = self.Reverse(list_s[i * k: i * k + k])
                else:
                    list_s[i * k: n] = self.Reverse(list_s[i * k: n])
            else:
                continue
        return "".join(list_s)

    def Reverse(self, list_slice):
        """
        :param list_slice: list
        :return: list
        """
        list_slice.reverse()
        return list_slice

if __name__ == "__main__":
    s = Solution()
    input = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    k = 39
    res = s.reverseStr(input, k)
    print(len(input))
    print(res)
    given = "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"
    assert res == given


