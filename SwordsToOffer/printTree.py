# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: printTree.py
time: 2018/8/30 14:37
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        if root == []:
            return []
        res = []
        res.append(root)
        ans = []
        while(res):
            ele = res.pop(0)
            ans.append(ele.val)
            if ele.left:
                res.append(ele.left)
            if ele.right:
                res.append(ele.right)
        return ans

def main():
    root = []
    s = Solution()
    res = s.PrintFromTopToBottom(root)
    print(res)

if __name__ == "__main__":
    main()