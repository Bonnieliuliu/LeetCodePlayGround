# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MaxDistanceOfBST.py
time: 2018/8/24 13:48

netease:
给定一棵二叉树，返回二叉树上距离最远的两个节点的距离
"""
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def MaxDistance(self, root):
        """

        :param root: TreeNode
        :return: max_distance: int
        """
        if not root.left and not root.right:
            return 0
        left = 0
        right = 0
        res = 0
        if root.left:
            left, res = self.MaxDistance(root.left, left, res)
            left += 1
        if root.right:
            right, res = self.MaxDistance(root.right, right, res)
            right +=1
        res = max(res, left+right+2)
        return max(left, right), res
