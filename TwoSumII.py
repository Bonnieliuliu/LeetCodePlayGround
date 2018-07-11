# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: TwoSumII.py
time: 2018/7/11 20:19
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        s = set()
        res = self.sumTarget(k, s, root)
        return res

    def sumTarget(self, k, s, root):
        if not root:
            return False
        if k - root.val in s:
            return True
        s.add(root.val)
        return self.sumTarget(k, s, root.left) or self.sumTarget(k, s, root.right)

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
        print(new.val)
        del parent_list[0]
    return tree
if __name__ == "__main__":
    s = Solution()
    array = [5,3,6,2,4,None,7]
    tree = list2tree(array)
    k = 9
    res = s.findTarget(tree[0], k)
    print(res)