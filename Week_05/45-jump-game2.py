# -*- coding: utf-8 -*-
# @Time : 2020/5/13 8:58
# @Author : edgar
# @FileName: 45-jump-game2.py.py
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        cur_max = nums[0]  # 初始化起点位置最远标记。
        end = nums[0]  # 记录到达最远标记，步数最少
        res = 1  # 记录最少次数
        if end >= len(nums) - 1:
            return res
        for i in range(1, len(nums)):
            cur_max = max(cur_max, i + nums[i])  # 更新最大值
            if i == end:  # 如果i走到了上一次跳跃可达到的最远点
                if end < len(nums) - 1:  # 如果这个end还没到最后一个位置，就跳一步，同时更新res和end
                    res += 1
                    end = cur_max
                    if end >= len(nums) - 1:  # 立刻判断新的end
                        return res
                else:
                    return res


class Solution3:
    def jump(self, nums: List[int]) -> int:
        reach, end, count = 0, 0, 0  # 初始化参数
        # 最后一位的计算没有意义，所以需要排除再外
        for i in range(len(nums) - 1):
            if reach >= i:
                reach = max(reach, i + nums)  # 更新最大值
                if i == end:  # 当到达可达值时则更新
                    end = reach
                    count += 1
        return count
