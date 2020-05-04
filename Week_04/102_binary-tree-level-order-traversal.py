# -*- coding: utf-8 -*-
# @Time : 2020/5/4 9:38
# @Author : edgar
# @FileName: 102_binary-tree-level-order-traversal.py

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        1.BFS
        2.DFS
        3.双端队列
        :param root:
        :return:
        """
        res = []
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root, 0)
        return res