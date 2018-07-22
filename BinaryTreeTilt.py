# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: BinaryTreeTilt.py
time: 2018/7/22 15:08
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return abs(self.GetSum(root.left)- self.GetSum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
    def GetSum(self, node):
        if not node:
            return 0
        return self.GetSum(node.left) + self.GetSum(node.right) + node.val

if __name__ == "__main__":
    s = Solution()
    from list2Tree import list2tree
    tree = list2tree([1,2,3])
    print(tree)
    res = s.findTilt(tree[0])
    print(res)
    assert res == 1