# -*- coding: utf-8 -*-
# @Time : 2020/7/2 21:14
# @Author : edgar
# @FileName: 145-binary-tree-postorder-traversal.py
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []

        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.right

            root = stack.pop()

            root = root.left

        return res[::-1]