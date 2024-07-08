# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]):
        new_tail = head if head else None

        def recur(head, head_next):
            if not head_next:
                return head
            new_head = recur(head_next, head_next.next)
            head_next.next = head
            return new_head

        new_head = recur(head, head.next)
        new_tail.next = None
        return new_head, new_tail

    def k_reverse(self, head: Optional[ListNode], k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, dummy
        flag = False
        iter = k
        while left:
            if flag:
                flag = False
                while right and iter > 0:
                    right = right.next
                    iter -= 1
                if not right: return dummy.next
                cache = right.next
                right.next = None
                new_head, new_tail = self.reverse(left.next)
                left.next = new_head
                new_tail.next = cache
                left = new_tail
                right = new_tail

            else:
                flag = True
                while right and iter > 0:
                    right = right.next
                    iter -= 1
                if not right: return dummy.next
                left = right
            iter = k
        return dummy.next


l = range(12)
nd_list = [ListNode(x) for x in l]
for i in range(11):
    nd_list[i].next = nd_list[i + 1]
head = nd_list[0]
a = Solution().k_reverse(head, 4)
print(a.val)
