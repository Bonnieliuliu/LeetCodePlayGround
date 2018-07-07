# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: IsValidPalindrome.py
time: 2018/7/7 14:51
"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            raise Exception("s is a empty string")
        if len(s) == 1:
            return True
        if len(s) == 2: # Whether s[0] == s[1] -->True or s[0]!= s[1],  remove s[0] or s[1] will do
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return (self.IsValidPalindrome(left, right - 1, s) or self.IsValidPalindrome(left + 1, right, s))
        return True
    def IsValidPalindrome(self, left, right, s):
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = "abdca"
    solu = Solution()
    res = solu.validPalindrome(s)
    print(res)