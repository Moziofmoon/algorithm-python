# -*- coding: utf-8 -*-
# @Time : 2020/4/28 20:12
# @Author : edgar
# @FileName: 78_subsets.py
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            newsets = []
            for sub in ans:
                newsets.append(sub + [num])
            ans.extend(newsets)

        return ans
