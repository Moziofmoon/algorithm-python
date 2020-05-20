# -*- coding: utf-8 -*-
# @Time : 2020/5/21 7:43
# @Author : edgar
# @FileName: 236-common-ancestor.py

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        # 当left 和 right 在root的不同侧时， 返回root
        return root