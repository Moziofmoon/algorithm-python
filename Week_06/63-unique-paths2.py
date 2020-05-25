# -*- coding: utf-8 -*-
# @Time : 2020/5/25 14:38
# @Author : edgar
# @FileName: 63-unique-paths2.py

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        定义状态：即数据元素的含义：dp表示当前位置的路径条数
        状态转移方程：dp[i] = dp[i] + dp[i - 1]
        设定初始值：增加初始值 1， 即 dp = [1] + [0] * n
        状态压缩：即优化数组空间，将二维数组压缩到一维数组，逐行计算当前最新路径条数，并覆盖上一行对应的路径条数
        选取dp[-2]表示到达finish
        障碍物： 1 有 0 没有
        :param obstacleGrid:
        :return:
        """

        # 行
        m = len(obstacleGrid)
        # 列
        n = len(obstacleGrid[0])
        # 压缩
        dp = [1] + [0]*n
        for i in range(0, m):
            for j in range(0, n):
                # 当有障碍物的时候，该步为0
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]

        return dp[-2]
