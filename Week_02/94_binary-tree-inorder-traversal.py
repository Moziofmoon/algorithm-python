# -*- coding: utf-8 -*-
# @Time : 2020/4/21 20:05
# @Author : edgar
# @FileName: 94_binary-tree-inorder-traversal.py
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        解题思路：递归
        :param root:
        :return:
        """
        f = self.inorderTraversal
        return f(root.left) + [root.val] + f(root.right) if root else []


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        解题思路：循环：利用两个栈，一个记录左子树的元素，一个记录答案
        时间复杂度：O(n)
        空间复杂度：O(n)
        :param root:
        :return:
        """
        if not root:
            return []

        stack = []
        ret = []

        # 将root遍历，且stack为空时
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret.append(root.val)
                root = root.right

        return ret
