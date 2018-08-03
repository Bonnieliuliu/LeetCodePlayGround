# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: list2Tree.py
time: 2018/7/11 20:38
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def list2tree(tree_list):
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
    return tree