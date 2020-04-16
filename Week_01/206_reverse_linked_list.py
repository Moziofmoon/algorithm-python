# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        解题思路：定义两个指针，前指针和当前指针，
                1.当前指针 指向下一个
                2.prev 记录 当前指针，为下个循环使用
                3.cur 移动至下一个
        :param head:
        :return:
        """

        if not head:
            return head
        prev = None
        cur = head
        # cur.next = prev 当前next指向前
        # prev = cur 将prve指向当前的指针
        # cur = cur.next 将cur的指针指向下一个
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
