# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(None)
        res = ListNode(None)
        pre_head.next = res
        carry = 0
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                res.val = sum % 10
            else:
                carry = 0
                res.val = sum
            if l1 or l2 or carry is not 0:
                res.next = ListNode(None)
                res = res.next
        return pre_head.next


l11 = ListNode(9)
l12 = ListNode(9)
l13 = ListNode(9)

l11.next = l12
l12.next = l13

l21 = ListNode(9)
l22 = ListNode(9)

l21.next = l22

Solution().addTwoNumbers(l11, l21)


class Solution2:
    def addTwoNumbers(self, l1: str, l2: str) -> str:
        it1, it2, carry = len(l1) - 1, len(l2) - 1, 0
        res = ""
        while it1>=0 or it2>=0 or carry:
            sum = carry
            if it1 >= 0:
                sum += int(l1[it1])
                it1 -=1
            if it2 >= 0:
                sum += int(l2[it2])
                it2 -= 1
            if sum >9:
                carry = 1
            else:
                carry = 0
            res = str(sum%10)+res
        return res

    def addTwoNumbers2(self, l1: str, l2: str) -> str:
        it1, it2, carry = len(l1) - 1, len(l2) - 1, 0
        res = ""
        while it1>=0 or it2>=0:
            sum = carry
            if it1 >= 0:
                sum += int(l1[it1])
                it1 -=1
            if it2 >= 0:
                sum += int(l2[it2])
                it2 -= 1
            if sum >9:
                carry = 1
            else:
                carry = 0
            res = str(sum%10)+res
        return "1"+res if carry else res

print(Solution2().addTwoNumbers("51189","967895"))

print(Solution2().addTwoNumbers2("51189","967895"))

