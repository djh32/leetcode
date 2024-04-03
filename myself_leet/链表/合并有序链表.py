#coding=utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def merge_sorted_list(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        t = ListNode(None)
        iter = t
        while head_1 and head_2:
            if head_1.val <= head_2.val:
                iter.next = head_1
                head_1 = head_1.next
            else:
                iter.next = head_2
                head_2 = head_2.next
            iter = iter.next
        if head_1:  # left node
            iter.next = head_1
        if head_2:  # left node
            iter.next = head_2
        return t.next




h10 = ListNode(1)
h11 = ListNode(2)
h12 = ListNode(4)
h13 = ListNode(6)
h10.next = h11
h11.next = h12
h12.next = h13

h20 = ListNode(5)

r = Solution().merge_sorted_list(h10, h20)
print(k)
