# -*- coding: utf-8 -*-
# @Time : 2020/7/4 17:47
# @Author : edgar
# @FileName: 101-symmetric-tree.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left, right):
            # 同时为空时
            if not (left or right):
                return True
            # 有一个为空而另一个不为空
            if not (left and right):
                return False

            # 均不为空
            if left.val != right.val:
                return False
            # 需要左右子树同时满足
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
