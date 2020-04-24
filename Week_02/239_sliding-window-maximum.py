# -*- coding: utf-8 -*-
# @Time : 2020/4/23 19:44
# @Author : edgar
# @FileName: 239_sliding-window-maximum.py
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        解题思路：
        一、明确题意：求滑动窗口内的最大值，窗口每次移动一位.
                    返回每个滑动窗口的最大值（list）
        1.暴力法 遍历每个滑动窗口，找到每个窗口的最大值。一共有N -k + 1个滑动窗口，
          每个有k个元素，于是算法的时间复杂度为O(Nk)
        2.堆 因为在最大中heap[0]永远是最大的元素，所以在k堆中插入元素的时间复杂度为log（k）
          所以算法的时间复杂度是O(NlogK)
        3.双端队列 时间复杂度 O（N） 空间复杂度 O（N）
        4.动态规划
        :param nums:
        :param k:
        :return:
        """

        n = len(nums)
        if not n * k:
            return []

        return [max(nums[i: i+k]) for i in range(n - k + 1)]


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        解题思路：
        一、明确题意：求滑动窗口内的最大值，窗口每次移动一位.
                    返回每个滑动窗口的最大值（list）
        1.暴力法 遍历每个滑动窗口，找到每个窗口的最大值。一共有N -k + 1个滑动窗口，
          每个有k个元素，于是算法的时间复杂度为O(Nk)
        2.堆 因为在最大中heap[0]永远是最大的元素，所以在k堆中插入元素的时间复杂度为log（k）
          所以算法的时间复杂度是O(NlogK)
        3.双端队列 时间复杂度 O（N） 空间复杂度 O（N）
        4.动态规划
        :param nums:
        :param k:
        :return:
        """

        n = len(nums)
        if not n * k:
            return []

        ret = []
        for i in range(n - k + 1):
            num = [-num for num in nums[i: i + k]]
            heapq.heapify(num)
            ret.append(-num[0])

        return ret


if __name__ == '__main__':
    solution = Solution2()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
