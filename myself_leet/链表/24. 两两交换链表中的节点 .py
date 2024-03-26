# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None)
        prev.next = head
        rtn = prev
        while prev != None:
            cur = prev.next
            if cur == None:
                return rtn.next
            tail = cur.next
            if tail == None:
                return rtn.next
            # reverse
            records = tail.next
            tail.next = cur
            cur.next = records
            prev.next = tail
            prev = cur
        return rtn.next

p =ListNode(None)
n = p
for i in range(4):
    p.next = ListNode(i)
    p = p.next
Solution().swapPairs(n.next)