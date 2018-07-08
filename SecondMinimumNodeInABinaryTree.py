# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: SecondMinimumNodeInABinaryTree.py
time: 2018/7/8 14:49
"""

import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        first = root.val
        second = sys.maxsize
        second_can = self.SecondMinimumValue(root, first, second)
        if second_can == first or second_can == second:
            return -1
        return second_can


    def SecondMinimumValue(self, node, first, second):

        if not node:
            return second
        if not node.val:
            return second
        if node.val > first and node.val < second:
            second = node.val
        second = self.SecondMinimumValue(node.left, first, second)
        second = self.SecondMinimumValue(node.right, first, second)
        return second

if __name__ == "__main__":
    tree_list = [2, 2, 5,None,None, 5,7]
    parent_list = []
    tree = []
    new = TreeNode(tree_list[0])
    del tree_list[0]
    parent_list.append(new)
    while parent_list:
        new = parent_list[0]
        if not new.left:
            if tree_list:
                left_son = TreeNode(tree_list[0])
                new.left = left_son
                del tree_list[0]
                parent_list.append(left_son)
            else:
                pass
        if not new.right:
            if tree_list:
                right_son = TreeNode(tree_list[0])
                new.right = right_son
                del tree_list[0]
                parent_list.append(right_son)
            else:
                pass
        tree.append(new)
        del parent_list[0]

    s = Solution()
    res = s.findSecondMinimumValue(tree[0])
    print(res)