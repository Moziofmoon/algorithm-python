# -*- coding: utf-8 -*-
# @Time : 2020/5/12 9:46
# @Author : edgar
# @FileName: 55-jump-game.py
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i, jump in enumerate(nums):
            # 当max_i > i 时，即表示可到达
            if max_i >= i and i + jump>max_i: # i 为当前位置，jump是当前位置的跳数
                max_i = i + jump # 更新最远能到达的位置

        return max_i >= i


if __name__ == '__main__':
    solution = Solution()
    sol = solution.canJump([1, 2, 3])
    print(sol)

