# coding=utf-8
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        l, r = dummy,dummy
        while n > 0:
            r = r.next
            n -=1
        while r.next != None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next

temp = [ListNode(x) for x in range(12)]
for i in range(11):
    temp[i].next = temp[i+1]
nd = Solution().removeNthFromEnd(temp[0],3)
print(nd)

