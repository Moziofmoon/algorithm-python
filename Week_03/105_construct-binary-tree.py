# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not len(inorder):
            return

        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以直接根据值查找中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        # 获取中序遍历root的节点，即前面的前面的节点均为左子树（计数n），
        # 则在前序遍历中，range(1, n+1)为左子树
        root.left = self.buildTree(preorder[1:mid +1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root



