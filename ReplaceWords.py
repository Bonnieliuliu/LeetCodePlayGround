"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = ReplaceWords.py
time = 2018/8/4 15:48
more information
"""
class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        word_to_root = {}
        sentence = sentence.split(" ")
        for word in sentence:
            word_to_root[word] = []
            for root in dict:
                if word.startswith(root):
                    word_to_root[word].append(root)
        output = []
        for word in sentence:
            if not word_to_root[word]:
                output.append(word)
            else:
                word_to_root[word].sort()
                output.append(word_to_root[word][0])
        return " ".join(output)