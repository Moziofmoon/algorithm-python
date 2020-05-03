# -*- coding: utf-8 -*-
# @Time : 2020/4/26 9:11
# @Author : edgar
# @FileName: 22_generate-parentheses.py
from typing import List


def generate1(level: int, MAX: int, s: str):
    # terminator 判断结束条件
    if level >= MAX:
        # 在此判断生产的合法性
        return
    # process 处理当前逻辑
    s1 = s + "("
    s2 = s + ")"
    # drill down
    generate1(level + 1, MAX, s1)
    generate1(level + 1, MAX, s2)
    # 优化方案
    # generate(level + 1, MAX, s + "(")
    # generate(level + 1, MAX, s + ")")


    # reverse state 初始化状态
    pass


def generate2(ret: List[str], left: int, right, n: int, s: str):
    # terminator 判断结束条件
    if left == n and right == n:
        ret.append(s)
        return
    # process 处理当前逻辑(合并至drill down)
    # drill down
    # 判断合法性：
    # 1.左括号随时可以+， 数量少于n
    # 2.右括号之前必须有左括号
    if left < n:
        generate2(ret, left + 1, right, n, s + "(")
    if right < left:
        generate2(ret, left, right + 1, n, s + ")")

    # reverse state 初始化状态

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        generate2(ret, 0, 0, n, "")
        return ret


if __name__ == '__main__':
    soultion = Solution()
    print(soultion.generateParenthesis(3))
    