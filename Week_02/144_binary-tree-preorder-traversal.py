# -*- coding: utf-8 -*-
# @Time : 2020/4/25 7:45
# @Author : edgar
# @FileName: 144_binary-tree-preorder-traversal.py

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        解题方法：
        1.递归
        2.迭代
        Note：注意返回条件
        :param root:
        :return:
        """
        if not root:
            return []
        f = self.preorderTraversal
        return [root.val] + f(root.left) + f(root.right)


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        解题方法：
        1.递归
        2.迭代
        :param root:
        :return:
        """
        if not root:
            return []

        stack = []
        ret = []
        while root or stack:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.left

            root = stack.pop().right

        return ret


class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """迭代法简单写法"""
        if not root:
            return []

        ret = []
        stack = []
        while root or stack:
            if root:
                ret.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()

        return ret