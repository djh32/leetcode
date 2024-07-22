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

    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        # dummy.next = head 这道题的难点在这里，如果给next=head的话，[4,2,1,3] 最后的4会没有空
        # 而且因为是插入算法，所以一开始的dummy就应该是空
        while head:
            save = head.next
            r1, r2 = dummy, dummy.next
            while r2 and r2 != head and r2.val < head.val:
                r1, r2 = r2, r2.next
            r1.next = head
            head.next = r2
            head = save
        return dummy.next


nd_list = [ListNode(x) for x in [4, 2, 1, 3]]
for i in range(3):
    nd_list[i].next = nd_list[i + 1]

r = Solution().insertionSortList2(nd_list[0])
print(r)
