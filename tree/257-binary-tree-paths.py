# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_path(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点为叶子节点时，添加路径
                    paths.append(path)
                else:
                    path += '->'
                    construct_path(root.left, path)
                    construct_path(root.right, path)

        paths = []
        construct_path(root, '')
        return paths