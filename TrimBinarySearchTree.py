# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: TrimBinarySearchTree.py
time: 2018/7/9 21:42
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root.val:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


if __name__ == "__main__":
    tree_list = [3, 0, 4, None, 2, None, None, 1, None]
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
    res = s.trimBST(tree[0], 1, 3)
    def PrintTree(root):
        if (not root) or (not root.val):
            return
        stack = []
        stack.append(root)
        while stack:
            print(stack)
            root = stack[0]
            if root.left and root.left.val:
                stack.append(root.left)
            if root.right and root.right.val:
                stack.append(root.right)
            print(root.val)
            print(stack)
            del stack[0]
        return
    PrintTree(res)
    res = [[None] * 2] * 5
    print(res)
