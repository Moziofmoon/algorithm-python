# -*- coding: utf-8 -*-
# @Time : 2020/5/23 7:36
# @Author : edgar
# @FileName: 76-mini_substring.py

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1
        t_len = len(t)

        minLeft, minRight = 0, len(s)
        left = 0

        for right, char in enumerate(s):
            # 看char是否在t中
            if mem[char] > 0:
                t_len -= 1
            mem[char] -= 1

            # 当t_len 为0 时，即表示找到答案的长度
            if t_len == 0:
                # 当该字符不在T中时，cnt< 0,起始点往后移
                while mem[s[left]] < 0:
                    mem[s[left]] += 1
                    left += 1

                if right - left < minRight - minLeft:
                    minLeft, minRight = left, right
                # 该点已经处理过，所以改变该点所处的条件
                mem[s[left]] += 1
                t_len += 1
                left += 1
        return '' if minRight == len(s) else s[minLeft:minRight + 1]


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1
        t_len = len(t)

        minLeft, minRight = 0, len(s)
        left = 0

        for right, char in enumerate(s):
            if mem[char] > 0:
                t_len -= 1
            mem[char] -= 1

            if not t_len:
                while mem[s[left]] < 0:
                    mem[s[left]] += 1
                    left += 1

                if right - left < minRight - minLeft:
                    minLeftm, minRight = left, right

                mem[s[left]] += 1
                t_len += 1
                left += 1

        return '' if minRight == len(s) else s[minLeft: minRight + 1]
