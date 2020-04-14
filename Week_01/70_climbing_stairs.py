# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        解题思路：f(n) = f(n-1) + f(n-2),可用递归，但是时间复杂度较高
                则利用常数替换函数
        时间复杂度：O(n)
        空间复杂度：O(1)
        :param n:
        :return:
        """
        first = 1
        second = 2
        if not n:
            return n
        if n == 1:
            return first
        if n == 2:
            return second
        ret = 0
        for i in range(n - 2):
            ret = first + second
            first, second = second, ret
        return ret
# leetcode submit region end(Prohibit modification and deletion)
