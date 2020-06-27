# -*- coding: utf-8 -*-
# @Time : 2020/6/24 8:18
# @Author : edgar
# @FileName: 72-edit-distance.py
from collections import deque


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 初始化变量 visit 存储字符串的值
        visit, q = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = q.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                d += 1
                q.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])

if __name__ == '__main__':
    solution = Solution()
    d = solution.minDistance("hello", "ell")
    print(d)