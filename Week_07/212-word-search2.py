# -*- coding: utf-8 -*-
# @Time : 2020/6/3 11:03
# @Author : edgar
# @FileName: 212-word-search2.py
from typing import List


class Solution:
    def findWords(self, board, words):
        WORD_END = '#'
        self.memo = {}

        for word in words:
            cur_node = self.memo
            for letter in word:  # 下面三行等效于cur_node=setdefault(letter,{})
                if letter not in cur_node:
                    cur_node[letter] = {}  # 新建一个
                cur_node = cur_node[letter]  # 不管有没有，进一位
            cur_node[WORD_END] = word  # 表示这个单词结束,记录单词日后好调用

        row_num = len(board)
        column_num = len(board[0])

        ans = []

        def backtrack(row, col, parent):
            # 下一个字母
            letter = board[row][col]
            cur_node = parent[letter]

            if WORD_END in cur_node:
                ans.append(cur_node[WORD_END])  # 当时记录的是那个完整单词
                cur_node.pop(WORD_END)  # 剪枝

            board[row][col] = '#'  # 代表被占用了，防止后续转回来

            for (delta_x, delta_y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_x, col + delta_y
                if not (0 <= next_row < row_num and 0 <= next_col < column_num):
                    continue
                elif board[next_row][next_col] not in cur_node:
                    continue
                else:
                    backtrack(next_row, next_col, cur_node)

            board[row][col] = letter  # 还原回去

            if not cur_node:  # 这个是剪枝，从后往前剪枝
                parent.pop(letter)

        for row in range(row_num):
            for col in range(column_num):
                if board[row][col] in self.memo:
                    backtrack(row, col, self.memo)

        return ans
