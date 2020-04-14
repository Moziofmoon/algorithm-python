# -*- coding: utf-8 -*-
# @Time : 2020/4/14 9:56
# @Author : edgar
# @FileName: 11_most_water.py

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
#  示例：
#
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        解题思路：初始化两个指针，分别指向数组的两端。计算其与x轴包围的面积。移动较小的一边，并计算面积。
                通过ret记录最大值
        时间复杂度：O(n)
        空间复杂度: O(1)
        :param height:
        :return:
        """

        # 初始化两个指针，分别指向数组的两端
        left = 0
        right = len(height) - 1

        # 初始化最大值
        ret = 0

        while left < right:
            # 计算面积
            area = (right - left) * min(height[right], height[left])
            ret = max(ret, area)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return ret

# leetcode submit region end(Prohibit modification and deletion)
