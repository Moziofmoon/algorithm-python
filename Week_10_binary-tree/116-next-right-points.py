# -*- coding: utf-8 -*-
# @Time : 2020/7/8 18:05
# @Author : edgar
# @FileName: 116-next-right-points.py

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root


import collections


class SolutionByQue:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)

            for i in range(size):
                node = Q.popleft()

                # 当i不是最后一个时，指向Q的下一个节点
                if i < size - 1:
                    node.next = Q[0]
                # 判断是否有子节点，并加入队列
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return root
