# -*- coding: utf-8 -*-
# @Time : 2020/5/9 8:14
# @Author : edgar
# @FileName: 47-permutations2.py
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, depth, used):
            if depth == len(nums):
                ret.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, path, depth + 1, used)
                    used[i] = False
                    path.pop()

        # 剪枝的前提是排序
        nums.sort()
        used = [False] * len(nums)
        ret = []
        dfs(nums, [], 0, used)
        return ret
