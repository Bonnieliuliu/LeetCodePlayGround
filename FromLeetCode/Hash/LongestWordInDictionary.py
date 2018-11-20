# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: LongestWordInDictionary.py
time: 2018/8/4 2:02
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        res = set([''])
        longestWord = ''
        for word in words:
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord

def main():
    input = ["a","banana","app","appl","ap","apply","apple"]
    s = Solution()
    res = s.longestWord(input)
    print(res)

if __name__ == "__main__":
    main()