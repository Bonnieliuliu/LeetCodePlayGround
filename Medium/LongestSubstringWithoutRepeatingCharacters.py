"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = LongestSubstringWithoutRepeatingCharacters.py
time = 2018/8/11 23:04
more information
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxcount = 0
        used = {}
        start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                maxcount = max(maxcount, index - start + 1)
            used[char] = index
        return maxcount
