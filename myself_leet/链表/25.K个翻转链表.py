# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:  # 递归反转
    def recur_apply(self, head, tail):
        def recur(head, nxt):
            if nxt == tail:
                new_head = tail
                nxt.next = head
                return head, new_head
            _, new_head = recur(nxt, nxt.next)
            nxt.next = head
            return head, new_head

        new_tail, new_head = recur(head, head.next)
        return new_head, new_tail

    def k_batch_reverse(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        left, right = dummy,dummy
        while left:
            for i in range(k):
                right = right.next
                if not right:
                    return dummy.next
            right_next = right.next
            new_head, new_tail = self.recur_apply(left.next, right)
            left.next = new_head
            new_tail.next = right_next
            left = new_tail
            right = new_tail
        return dummy.next


h0 = ListNode(0)
h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h0.next = h1
h1.next = h2
h2.next = h3

r = Solution2().k_batch_reverse(h0,1)

print(r)


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
        cur.next = prev  # 注意这里可能会断
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

for i in range(1, 6):
    prev.next = ListNode(i)
    prev = prev.next

Solution().reverseKGroup(prev2.next, 1)
