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

    def sortList(self, head: ListNode) -> ListNode:
        def recurrent_iter(head,tail):
            if not head:
                return head
            slow,fast = head,head
            while fast:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            mid = slow

            right = mid.next
            mid.next = None

            return self.merge_sorted_list(recurrent_iter(head,mid),recurrent_iter(right,tail))
        return recurrent_iter(head,None)