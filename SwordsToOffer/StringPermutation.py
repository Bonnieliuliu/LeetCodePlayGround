'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
'''
solution:
固定第一个位置的元素i，求剩余位置的所有排列 permutation(ss[0:i] + ss[i+1:]), concate i + permutation(ss[0:i] + ss[i+1:])

for i in range(len(ss)):
    ss[i] + permutation(ss[:i] + ss[i+1:])
'''

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return ss
        res = []
        for i in range(len(ss)):
            head = ss[i]
            shadow = ss[:i]+ss[i+1:]
            for j in self.Permutation(shadow):
                res.append(head + j)
        return sorted(list(set(res)))