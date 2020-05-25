# -*- coding: utf-8 -*-
# @Time : 2020/5/26 7:38
# @Author : edgar
# @FileName: 1143-common-substring.py

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # if n < m:
        #     text1, text2 = text2, text1
        dp = [0 for i in range(m+1)]
        tmp = dp[:]
        for i in text1:
            for j, ch in enumerate(text2):
                if i == ch:
                    dp[j] = tmp[j-1] + 1
                else:
                    dp[j] = max(tmp[j],dp[j-1])
            # dp 相当于当前行
            # tmp 相当于上一行
            tmp, dp = dp, tmp
        return tmp[-2]


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] != text2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                else:
                    dp[i+1][j+1] = dp[i][j] + 1
        return dp[-1][-1]


if __name__ == '__main__':
    soultion = Solution()
    sol = soultion.longestCommonSubsequence('abcde', 'ace')
    print(sol)
