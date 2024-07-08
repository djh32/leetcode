# Definition for singly-linked list.
from typing import Optional

"""
143. 重排链表
中等
相关标签
相关企业
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getMidNode(self,head):
        dummy = ListNode(0)
        dummy.next = head
        slow,fast = dummy,dummy
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def recurReverse(self,head):
        new_tail = head
        def recur(head,head_next):
            if head_next is None:
                return head
            newhead = recur(head_next,head_next.next)
            head_next.next = head
            return newhead
        new_head = recur(head,head.next)
        new_tail.next = None
        return new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return head
        mid = self.getMidNode(head)
        part2 = self.recurReverse(mid.next)
        mid.next = None

        dummy = ListNode(0)
        flag = True
        dummy.next = head
        while head and part2:
            if flag:
                new_head = head.next
                head.next = part2
                head = new_head
                flag = False
            else:
                new_part2 = part2.next
                part2.next = head
                part2 = new_part2
                flag = True
        return dummy.next

tp = [ListNode(x) for x in range(1)]
for i in range(0):
    tp[i].next = tp[i+1]

head= Solution().reorderList(tp[0])
print(head)













