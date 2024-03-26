# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        def findMid(node) -> ListNode:
            s = node
            f = node.next
            if not f:
                return s

            while s and f:
                s = s.next
                for _ in range(2):
                    if f:
                        f = f.next
                    else:
                        return s
            return s

        mid = findMid(head)
        midReverse = reverse(mid)
        while midReverse:
            if head.val != midReverse.val:return False
            head = head.next
            midReverse = midReverse.next
        return True


prev = ListNode(None)
prev2 = prev

for i in [1,2,3,3,4,3,3,2,1]:
    prev.next = ListNode(i)
    prev = prev.next

print(Solution().isPalindrome(prev2.next))
