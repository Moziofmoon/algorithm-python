# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        解题思路：查找非0索引，并按顺序将非0索引，放置再数组前列，后面的位数用0补足
        时间复杂度： O(n)
        空间复杂度： O(n)
        """

        pos = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        nums[pos:] = [0] * (len(nums) - pos)


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        解题思路：通过快慢指针，快指针每次均前进一步。慢指针在非0时前进一步，
        当慢指针为0，快指针非0时，交换
        时间复杂度： O(n)
        空间复杂度： O(n)
        """

        slow = fast = 0

        while fast < len(nums):
            if not nums[slow] and nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # 查找 0
            if nums[slow]:
                slow += 1

            # fast keep going
            fast += 1
