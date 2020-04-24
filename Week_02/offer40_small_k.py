# -*- coding: utf-8 -*-
# @Time : 2020/4/22 8:51
# @Author : edgar
# @FileName: offer40_small_k.py
import heapq
from typing import List


class Solution:
    """
    方法一：暴力法（sort） 时间复杂度：O(n logn)
    方法二：堆 时间复杂度 O(n logk)
    方法三：快排分区 时间复杂度 O(n) 最坏 O(n^2)
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)               # 初始化堆->最大堆
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])

        ret = [-x for x in hp]
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.getLeastNumbers([3,2,1], 2))
