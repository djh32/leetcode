# Definition for singly-linked list.
from typing import Optional

"""
奇数index 的是正序
偶数index 的是倒序

给出正序list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMidNode(self, head):
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def recurReverse(self, head):
        new_tail = head

        def recur(head, head_next):
            if head_next is None:
                return head
            newhead = recur(head_next, head_next.next)
            head_next.next = head
            return newhead

        new_head = recur(head, head.next)
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


def merge_sort(h1, h2):
    dm = h = ListNode()

    while h1 and h2:
        if h1.val < h2.val:
            h.next, h1 = h1, h1.next
        else:
            h.next, h2 = h2, h2.next
        h = h.next
    h.next = h1 if h1 else h2
    return dm.next


def sort_list(head):
    dm1 = h1 = ListNode(0)
    dm2 = h2 = ListNode(0)
    flag = True
    while head:
        if flag:
            h1.next = head
            h1 = h1.next
            flag = False
        else:
            h2.next = head
            h2 = h2.next
            flag = True
        head = head.next
    h1.next = None
    h2.next = None
    # merge h1,reverse(h2)
    h2 = Solution().recurReverse(dm2.next)
    h1 = dm1.next

    st = merge_sort(h1,h2)
    return st


tp = [ListNode(x) for x in range(8)]
for i in range(7):
    tp[i].next = tp[i + 1]

head = Solution().reorderList(tp[0])
print(head)

hd = sort_list(head)
print(hd)
