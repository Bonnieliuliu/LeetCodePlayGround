# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: LongestUnivaluePath.py
time: 2018/7/6 12:53
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        _, res = self.Path(root, 0)
        return res

    def Path(self, son, res):
        if not son:
            return 0
        if son.left:
            left, res = self.Path(son.left, res)
        if son.right:
            right, res = self.Path(son.right, res)
        if son.left and son.val == son.left.val:
            left = left + 1
        else:
            left = 0
        if son.right and son.val == son.right.val:
            right = right + 1
        else:
            right = 0
        res = max(left + right, res)
        return max(left, right), res


if __name__ == "__main__":
    tree_list = [1,4,5,4,4,5]
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
    res = s.longestUnivaluePath(tree[0])
    print(res)