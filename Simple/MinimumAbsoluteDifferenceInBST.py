# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MinimumAbsoluteDifferenceInBST.py
time: 2018/7/30 0:29
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys


class Solution:

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre = -1
        res = sys.maxsize
        pre, res = self.inorder(root, pre, res)
        return res

    def inorder(self, node, pre, res):
        if not node:
            return pre, res
        pre, res = self.inorder(node.left, pre, res)
        if pre != -1:
            res = min(res, node.val - pre)
        pre = node.val
        pre, res = self.inorder(node.right, pre, res)
        return pre, res


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            print(line)
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().getMinimumDifference(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()