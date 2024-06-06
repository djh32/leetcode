# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        step_a, step_b = headA, headB
        while step_a != step_b and (step_a.next != None or step_b.next != None):
            if step_a.next == None:
                step_a = headB
                step_b = step_b.next
                continue
            if step_b.next == None:
                step_b = headA
                step_a = step_a.next
                continue
            else:
                step_a = step_a.next
                step_b = step_b.next
                continue
        if step_a == step_b:
            return step_a
        else:
            return None


l1 = [ListNode(i) for i in [2, 6, 4]]
for idx in range(len(l1) - 1):
    l1[idx].next = l1[idx + 1]
head_A = l1[0]

l1 = [ListNode(i) for i in [1, 5]]
for idx in range(len(l1) - 1):
    l1[idx].next = l1[idx + 1]
head_B = l1[0]

Solution().getIntersectionNode(head_A, head_B)
