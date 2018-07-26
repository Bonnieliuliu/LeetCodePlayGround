# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: List2LinkedList.py
time: 2018/7/27 0:13
"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class List2LinkedList():
    @staticmethod
    def list2LinkedList(list1):
        first = ListNode(list1[0])
        output = first
        del list1[0]
        for ele in list1:
            l = ListNode(ele)
            output.next = l
            output = output.next
        return first
    @staticmethod
    def printLinkedList(l1):
        while l1:
            print(l1.val)
            l1 = l1.next