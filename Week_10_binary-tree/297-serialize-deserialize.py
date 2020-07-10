# -*- coding: utf-8 -*-
# @Time : 2020/7/10 8:12
# @Author : edgar
# @FileName: 297-serialize-deserialize.py
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append("#")

        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        parts = data.split(",")

        idx = 0
        val = parts[idx]

        if val == "#":
            return None

        root = TreeNode(int(val))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # 增加左子树
            idx += 1
            val = parts[idx]
            if val != "#":
                node.left = left = TreeNode(int(val))
                queue.append(left)

            # 增加右子树
            idx += 1
            val = parts[idx]
            if val != "#":
                node.right = right = TreeNode(int(val))
                queue.append(right)

        return root


