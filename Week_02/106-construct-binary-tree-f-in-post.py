# -*- coding: utf-8 -*-
# @Time : 2020/7/5 21:34
# @Author : edgar
# @FileName: 106-construct-binary-tree-f-in-post.py
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        return root


if __name__ == '__main__':
    solution = Solution()
    solution.buildTree([9,3,15,20,7], [9,15,7,20,3])
