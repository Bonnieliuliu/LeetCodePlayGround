# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MergeTwoBinaryTrees.py
time: 2018/7/15 2:19
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or t1.val:
            return t2
        if not t2 or t2.val:
            return t1
        val = t1.val + t2.val
        t = TreeNode(val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        return t

# if __name__ == "__main__":
#     from list2Tree import list2tree
#     s = Solution()
#     input1 = [1,3,2,5]
#     input2 = [2,1,3,None,4,None,7]
#     input1 = list2tree(input1)
#     input2 = list2tree(input2)
#     res = s.mergeTrees(input1[0], input2[0])
#     print(res.val)