"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = ValidPalindrome.py
time = 2018/8/11 22:13
more information
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while (left < right):
            if not self.isValidInput(s[left]):
                left += 1
            elif not self.isValidInput(s[right]):
                right -= 1
            elif s[left].upper() != s[right].upper():
                return False
            else:
                left += 1
                right -= 1
        return True

    def isValidInput(self, char):
        if char.upper() >= "A" and char.upper() <= "Z":
            return True
        if char >= "0" and char <= "9":
            return True
        return False