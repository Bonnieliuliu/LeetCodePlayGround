# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PartitionList.py
time: 2018/8/8 22:15
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:(wrong)
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         dummy = ListNode(-1)
#         dummy.next = head
#         pre = dummy
#         cur = dummy
#         while(pre.next and pre.next.val>=x):
#             cur = pre
#         while(cur.next):
#             if cur.next.val<x:
#                 tmp = cur.next
#                 cur.next = tmp.next
#                 tmp.next = pre.next
#                 pre.next = tmp
#                 pre = pre.next
#             else:
#                 cur = cur.next
#         return dummy.next



class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None or head.next is None or x is None:
            return head

        p1 = head1 = ListNode(0)
        p2 = head2 = ListNode(0)
        p = head

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = head2.next
        p2.next = None
        return head1.next