# -*- coding: utf-8 -*-
# @Time : 2020/5/20 7:47
# @Author : edgar
# @FileName: 1371-find-long-substring.py


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        l, ans, state = [0] + [-1] * 31, 0, 0
        for i in range(len(s)):
            # 位运算，当该位有值时，则为单数
            if s[i] in 'aeiou': state ^= 1 << 'aeiou'.find(s[i])
            # 当为初始值（即未出现奇数次元音字母时），则修改状态
            # if中 负数为True
            # 当字符串中不含有元音字母时，可以计数
            if ~l[state]:
                # 更新为当前下标-最早的下标
                ans = max(ans, i + 1 - l[state])
            else:
                # l[state] 表示最早的下标
                l[state] = i + 1
        return ans


if __name__ == '__main__':
    soultion = Solution()
    soultion.findTheLongestSubstring("beleetminicoworoep")

