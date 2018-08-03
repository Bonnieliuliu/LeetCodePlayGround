# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: AverageOfLevelsInBinaryTree.py
time: 2018/7/13 1:01
"""
# Definition for a binary tree node.
from list2Tree import list2tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        parent_list_1 = [root]
        parent_list_2 = []
        average = []
        while parent_list_1 or parent_list_2:
            level_sum = 0
            count = 0
            while parent_list_1:
                root = parent_list_1[0]
                level_sum += root.val
                if root.left:
                    parent_list_2.append(root.left)
                if root.right:
                    parent_list_2.append(root.right)
                del parent_list_1[0]
                count += 1
            if count != 0:
                average.append(level_sum / count)
            level_sum = 0
            count = 0
            while parent_list_2:
                root = parent_list_2[0]
                level_sum += root.val
                if root.left:
                    parent_list_1.append(root.left)
                if root.right:
                    parent_list_1.append(root.right)
                del parent_list_2[0]
                count += 1
            if count != 0:
                average.append(level_sum / count)
        return average

if __name__ == "__main__":
    list1 = [3,9,20,15,7]
    tree1 = list2tree(list1)
    s = Solution()
    res = s.averageOfLevels(tree1[0])
    print(res)