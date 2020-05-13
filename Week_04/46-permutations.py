# -*- coding: utf-8 -*-
# @Time : 2020/5/8 7:42
# @Author : edgar
# @FileName: 46-permutations.py
import itertools
from typing import List


class Solution:
    """
    方法一：直接递归
    方法二：回溯
    """
    def permute1(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        ret = []
        for idx, num in enumerate(nums):
            # 确定剩余元素
            res_nums = nums[:idx] + nums[idx + 1:]
            for j in self.permute(res_nums):
                ret.append([num] + j)

        return ret


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(solution, res, left):
            if not left:
                res.append(solution[:])
                return
            for i in range(len(left)):
                solution.append(left[i])
                helper(solution, res, left[:i] + left[i + 1:])
                solution.pop()

        res = []
        helper([], res, nums)
        return res


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯：树的深度遍历（选择，撤销选择，剪枝）
        def dfs(nums, path, depth, used):  # path变量是一个栈
            """

            :param nums: 原数组
            :param path: 栈
            :param depath: 当前深度
            :param used: 是否使用标记数组
            :return:
            """
            if depth == len(nums):  # 递归的终止条件是，数已经选够
                # 因为只用path一个变量，是指向一个内存空间，所以要用copy
                res.append(path[:])  # path[:] == path.copy()
                return  # 退出函数，不往下继续进行

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])  # 选择
                    used[i] = True # 代表该节点已经选择过

                    dfs(nums, path, depth+1, used)

                    path.pop()  # 撤销选择
                    used[i] = False

        res = []
        # 按顺序给数组标记为False
        used = [False for _ in range(len(nums))]
        dfs(nums, [], 0, used)

        return res


class Solution4:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

class Solution5:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


