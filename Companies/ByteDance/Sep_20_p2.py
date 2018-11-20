# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_20_p2.py
time: 2018/9/20 19:19
"""
class Solution(object):
    def Prefix(self, vocab):
        if not vocab:
            return None
        n = len(vocab)
        result = []
        for k in range(n):
            current_word = vocab[k]
            prefix = ""
            for i in range(len(current_word)):
                prefix += current_word[i]
                if self.OtherStartsWithSame(prefix, k, n, vocab):
                    continue
                else:
                    result.append(prefix)
                    break
        return result

    def OtherStartsWithSame(self, prefix, k, n, vocab):
        for j in range(n):
            if j != k and vocab[j].startswith(prefix):
                return True
            elif j!=k and not vocab[j].startswith(prefix):
                continue
            else:
                continue
        return False
def main():
    n = int(input().strip())
    vocab = []
    for i in range(n):
        line = str(input().strip())
        vocab.append(line)
    s = Solution()
    result = s.Prefix(vocab)
    for answer in result:
        print(answer)

if __name__ == "__main__":
    main()