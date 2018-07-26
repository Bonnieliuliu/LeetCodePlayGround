# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MergedTwoSortedLists.py
time: 2018/7/26 17:18
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        while (l1 and l2):
            if (l1.val <= l2.val):
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

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

if __name__ == "__main__":
    s = Solution()
    input1 = [1,2,3]
    l1 = List2LinkedList.list2LinkedList(input1)
    input2 = [1,2,4]
    l2 = List2LinkedList.list2LinkedList(input2)
    res = s.mergeTwoLists(l1, l2)
    List2LinkedList.printLinkedList(res)