# -*- coding: utf-8 -*-
# @Time : 2020/4/27 8:52
# @Author : edgar
# @FileName: 50_powx-n.py


class Solution:
    """
    解题步骤：
    1.确认面试题：
        （1） x， n 的范围
        （2） x, n 的数据类型（整数， 还是小数）
        （3） 能否用库函数
    2.思考解决方案
        （1）暴力法：循环累乘 O(n)
        （2）分治法： O(n)
            pow(x, n):
                subproblem: pow(x, n/2)

        （3）牛顿迭代法：
    """
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return x*self.myPow(x, n - 1)
        return self.myPow(x * x, n/2)