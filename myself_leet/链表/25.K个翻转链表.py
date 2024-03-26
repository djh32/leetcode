# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head, tail):
        prev = ListNode(None)
        prev.next = head
        cur = head
        newTail = head
        while cur != tail:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur.next = prev # 注意这里可能会断
        newHead = cur
        return newHead, newTail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = ListNode(None)
        prev.next = head
        new_p = prev
        cur = head
        tail = head
        if k == 1:
            return prev.next
        while new_p.next != None:
            for _ in range(k - 1):
                tail = tail.next
                if tail == None:
                    return prev.next
                reverListNext = tail.next
            subListHead, subListTail = self.reverse(cur, tail)
            new_p.next = subListHead
            subListTail.next = reverListNext
            new_p = subListTail
            cur = new_p.next
            tail = new_p.next
        return prev.next

prev = ListNode(None)
prev2 = prev

for i in range(1,6):
    prev.next = ListNode(i)
    prev = prev.next

Solution().reverseKGroup(prev2.next,1)




