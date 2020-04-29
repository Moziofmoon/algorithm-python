# -*- coding: utf-8 -*-
# @Time : 2020/4/29 7:40
# @Author : edgar
# @FileName: 51_n-qurens.py
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, diff_xy, sum_xy):
            rows = len(queens)
            if rows == n:
                result.append(queens)
                return

            for col in range(n):
                if col not in queens and rows - col not in diff_xy and rows + col not in sum_xy:
                    DFS(queens + [col], diff_xy + [rows - col], sum_xy + [rows + col])

        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n - i - 1) for i in sol] for sol in result]
