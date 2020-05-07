# -*- coding: utf-8 -*-
# @Time : 2020/5/7 9:15
# @Author : edgar
# @FileName: 529-minesweeper.py

# 让我们一起来玩扫雷游戏！
#
#  给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）
# 地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
#
#  现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
#
#
#  如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
#  如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
#  如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
#  如果在此次点击中，若无更多方块可被揭露，则返回面板。
#

#  注意：
#
#
#  输入矩阵的宽和高的范围为 [1,50]。
#  点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
#  输入面板不会是游戏结束的状态（即有地雷已被挖出）。
#  简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。
#  Related Topics 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class SolutionDFS:
    """
    1.如果click = M，结束
    2.如果不是，则进入循环
    """
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []

        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'x'
            return board
        self.dfs(board, i, j)
        return board

    def dfs(self, board, i, j):
        # 未被挖出的空方块，均为E
        if board[i][j] != "E":
            return

        # 定义长宽
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        mine_count = 0
        # 计算周围是否有炸弹
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            # 如果在棋盘内，而且是雷的，显示数量+1
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "M":
                mine_count += 1
        if not mine_count:
            board[i][j] = "B"
        else:
            board[i][j] = str(mine_count)
            return

        # 当未发现炸弹时，递归查找
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj)
