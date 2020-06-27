# -*- coding: utf-8 -*-
# @Time : 2020/6/22 7:53
# @Author : edgar
# @FileName: 493-reverse-pairs.py
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(low, high):
            if low + 1 >= high:
                return 0
            mid = (low + high) >> 1
            cnt = mergeSort(low, mid) + mergeSort(mid, high)

            j = mid
            for i in nums[low: mid]:
                while j < high and i > 2 * nums[j]:
                    j += 1
                cnt += j -mid

            nums[low: high] = sorted(nums[low: high])
            return cnt

        return mergeSort(0, len(nums))
