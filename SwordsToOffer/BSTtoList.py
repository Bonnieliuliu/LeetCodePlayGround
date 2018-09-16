# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: BSTtoList.py
time: 2018/8/30 1:15
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.head = ListNode(None)
        self.flag = False

    def BSTtoList(self, root):
        if not root:
            return None
        if not root.left and not root.right and not self.flag:
            self.head = ListNode(root.val)
            self.flag = True
            return self.head
        curnode = ListNode(root.val)
        left = self.BSTtoList(root.left)
        p = left
        while (p and p.next):
            p = p.next
        if left:
            p.next = curnode

        right = self.BSTtoList(root.right)
        curnode.next = right
        return left if left else curnode



def main():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    s = Solution()
    s.BSTtoList(root)
    print(s.head.val)
    print(s.head.next.val)
    print(s.head.next.next.val)
    print(s.head.next.next.next.val)

if __name__ == "__main__":
    main()


