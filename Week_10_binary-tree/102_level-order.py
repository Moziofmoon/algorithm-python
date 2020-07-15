# -*- coding: utf-8 -*-
# @Time : 2020/7/8 15:45
# @Author : edgar
# @FileName: 102_level-order.py
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 定义数组，每一层为一个元素
        nodes = [(root,)]
        values = []
        while nodes:
            values.append([r.val for n in nodes for r in n if r])
            nodes = [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]


class Solution2:
    def levelOrder(self, root):
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root:
            return root
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level+1, res)
        if root.right:
            self.level(root.right, level+1, res)


if __name__ == '__main__':
    soultion = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    soultion.levelOrder(root)