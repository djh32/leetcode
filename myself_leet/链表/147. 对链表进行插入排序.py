# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_insert(self, dummy, node):
        if not dummy.next: dummy
        before = dummy
        cur = dummy.next
        while cur and node.val > cur.val:
            before, cur = before.next, cur.next
        return before, cur

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        while head:
            cache = head.next
            before, after = self.get_insert(dummy, head)
            before.next = head
            head.next = after
            head = cache
        return dummy.next


h0 = ListNode(1)
h1 = ListNode(5)
h2 = ListNode(4)
h3 = ListNode(2)
h4 = ListNode(3)
h0.next = h1
h1.next = h2
h2.next = h3
h3.next = h4
r = Solution().insertionSortList(h0)
print(r)
