# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MiddleOfTheLinkedList.py
time: 2018/8/6 2:01
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        buf = []
        while(tmp):
            buf.append(tmp.val)
            tmp = tmp.next
        if len(buf) == 1:
            return head
        index = int((len(buf)-2)/2)+1
        i = 0
        tmp2 = head
        while(i<index):
            tmp2 = tmp2.next
            i += 1
        return tmp2