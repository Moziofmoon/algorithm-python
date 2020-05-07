from typing import List


class Solution:
    """
    解题思路：
        一、暴力法：计数后比较
    """
    def majorityElement(self, nums: List[int]) -> int:
        if not len(nums):
            return

        dic = {}
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1

        # 取value最大值
        return max(dic, key=dic.get)


class Solution2:
    """
    解题思路：
        二、暴力法：计数后比较
    """
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    soultion = Solution()
    print(soultion.majorityElement([3, 2, 3]))
