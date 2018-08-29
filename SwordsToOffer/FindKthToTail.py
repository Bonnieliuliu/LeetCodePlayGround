# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: FindKthToTail.py
time: 2018/8/29 23:48
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        p1 = head
        p2 = head
        while k > 1:
            if p1.next:
                p1 = p1.next
                k -= 1
            else:
                return None
        while(p1.next):
            p1 = p1.next
            p2 = p2.next
        return p2

def main():
    import sys
    raw = list(map(int, sys.stdin.readline().strip().split()))
    head = ListNode(raw[0])
    cur = head
    for i in range(1, len(raw)):
        cur.next = ListNode(raw[i])
        cur = cur.next

    k = 1
    s = Solution()
    res = s.FindKthToTail(head, k)
    print(res.val)

if __name__== "__main__":
    main()