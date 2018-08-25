# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: 3.py
time: 2018/8/25 10:58
"""
def readData():
    arr = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        n = sys.stdin.readline().strip()
        word1 = sys.stdin.readline().strip()
        word2 = sys.stdin.readline().strip()
        arr.append([word1, word2])
    return n, arr

def Main(n, arr):
    output = []
    for ele in arr:
        if IsShuang(ele[0], ele[1]):
            output.append("Yeah")
        else:
            output.append("Sad")
    return output

def IsShuang(word1, word2):
    if len(word1)!=len(word2):
        return False
    for i in range(len(word1)):
        bianxing = word1[i:]+word1[:i]
        if bianxing == word2:
            return True
        if bianxing[::-1] == word2:
            return True
    return False

import sys
if __name__ == "__main__":
    n, arr = readData()
    for ele in arr:
        res = IsShuang(ele[0], ele[1])
        if res:
            print("Yeah")
        else:
            print("Sad")
#     res = Main(n, arr)
#     for r in res:
#         print(r)