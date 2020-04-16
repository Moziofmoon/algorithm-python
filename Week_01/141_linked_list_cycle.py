# -*- coding: utf-8 -*-
# @Time : 2020/4/16 8:38
# @Author : edgar
# @FileName: 141_linked_list_cycle.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        解题思路：利用快慢指针，若快慢指针重合，则为环
        :param head:
        :return:
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True

        return False
