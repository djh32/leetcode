#coding=utf-8

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.new_head = None
    def reverse(self, head, tail):
        dummpy = ListNode(None)
        dummpy.next = head
        tail_reversed = head
        before,cur = head,head.next
        while cur:
            after = cur.next
            cur.next = before
            before = cur
            cur = after
        tail_reversed.next = None
        dummpy.next = before
        return dummpy.next

    def reverse2(self,head):
        dummy = ListNode(None)
        dummy.next = head
        before,cur = dummy,head
        new_tail = head
        while cur:
            after = cur.next
            cur.next = before
            before = cur
            cur = after
        new_tail.next = None
        return before

    def rever_recur(self,node,after):
        if not after:
            self.new_head = node
            return None
        self.rever_recur(after,after.next)
        after.next = node






h0 = ListNode(0)
h1 = ListNode(3)
h2 = ListNode(4)
h3 = ListNode(1)
h0.next = h1
h1.next=h2
h2.next = h3

dummy = ListNode(None)
dummy.next = h0
r = Solution()
r.rever_recur(dummy,h0)
h0.next = None
print(r.new_head)
