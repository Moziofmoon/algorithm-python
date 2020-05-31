# -*- coding: utf-8 -*-
# @Time : 2020/5/31 8:30
# @Author : edgar
# @FileName: 53-maximum-subarray.py
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 暴力求解：枚举任意起点和终点 优化一：只有正数
        """
        2.DP:
            a.分治（子问题）： max_sum(i) = max(max_sum(i - 1), 0) + a[i]
            b.状态数组定义 f[i]
            c.DP方程 f[i] = max(f[i-1], 0) + a[i]
        :param nums:
        :return:
        """

        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(0, nums[i - 1])

        return max(nums)
