# -*- coding: utf-8 -*-
# @Time : 2020/4/20 20:21
# @Author : edgar
# @FileName: 242_valid-anagram.py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        解题思路：暴力求解法（排序法）
        排序后判断是否相等。因排序算法为NlogN,所以时间复杂度为 NlogN
        :param s:
        :param t:
        :return:
        """
        return sorted(s) == sorted(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        解题思路：计算数法
        利用map记录字符的数量
        :param s:
        :param t:
        :return:
        """
        if set(s) == set(t):
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
        else:
            return False

        return True