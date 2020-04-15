# -*- coding: utf-8 -*-
# @Time : 2020/4/15 8:24
# @Author : edgar
# @FileName: 15_three_sum.py
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        解题思路：将数组分为三堆，通过map{num, cnt}存储。当输入值为负时，则在正数中计算第三个值
                对第三值的有效性进行验证
                假设：
                    1.当第一个数为正数时，则第二个数在负数中选择，第三个数为非正数（包含0）
                    2.当第一个数为负数时，同上
                    3.当为0时，需要计算0的个数
                验证：
                    1.当第三个数为正数时，需判断是否与第二数相等，且原数组中的cnt
                    2.当第三个数为0时，0的个数需大于3
        时间复杂度：O(nlong(n))
        空间复杂度：O(n)
        :param nums:
        :return:
        """
        # # 利用hashmap 存储 neg/pos 数字的个数
        # neg = {}
        # pos = {}
        # zeros = 0
        #
        # # 利用set保存结果元组
        # rets = set()
        #
        # # 初始化 计数器 O(n)
        # for i in nums:
        #     if i < 0:
        #         neg.setdefault(i, 0)
        #         neg[i] += 1
        #     elif i > 0:
        #         pos.setdefault(i, 0)
        #         pos[i] += 1
        #     else:
        #         zeros += 1
        # # 遍历set
        # for i in {num for num in nums}:
        #     # 当 i 为负数时， 则和在正数中取
        #     if i < 0:
        #         for j in pos:
        #             k = -i - j
        #             if k in pos:
        #                 # 当结果中有相同的值时，需要查看该值的个数
        #                 if k == j and pos[j] - 1 < 1:
        #                     continue
        #                 else:
        #                     rets.add(tuple(sorted((i, j, k))))
        #             elif k == 0 and zeros > 0:
        #                 rets.add(tuple(sorted((i, j, k))))
        #
        #
        #     # 下同
        #     elif i > 0:
        #         for j in neg:
        #             k = -i - j
        #             if k in neg:
        #                 if k == j and neg[j] - 1 < 1:
        #                     continue
        #                 else:
        #                     rets.add(tuple(sorted((i, j, k))))
        #             elif k == 0 and zeros > 0:
        #                 rets.add(tuple(sorted((i, j, k))))
        #
        #     elif zeros > 2:
        #         rets.add((0, 0, 0))
        #
        # return [list(s) for s in rets]

        neg = {}
        pos = {}
        zeros = 0

        ret = set()

        for num in nums:
            if num > 0:
                pos.setdefault(num, 0)
                pos[num] += 1
            elif num < 0:
                neg.setdefault(num, 0)
                neg[num] += 1
            else:
                zeros += 1

        for i in {num for num in nums}:
            if i > 0:
                for j in neg:
                    k = -i - j
                    if k in neg:
                        if k == j and neg[j] < 2:
                            continue
                        else:
                            ret.add(tuple(sorted((i, j, k))))
                    else:
                        if not k and zeros > 0:
                            ret.add(tuple(sorted((i, j, k))))
            elif i < 0:
                for j in pos:
                    k = -i - j
                    if k in pos:
                        if k == j and pos[j] < 2:
                            continue
                        else:
                            ret.add(tuple(sorted((i, j, k))))
                    else:
                        if not k and zeros > 0:
                            ret.add(tuple(sorted((i, j, k))))
            else:
                if zeros > 2:
                    ret.add((0, 0, 0))

        return [list(s) for s in ret]




if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    ret = solution.threeSum(nums)
    print(ret)
