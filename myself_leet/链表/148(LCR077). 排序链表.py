class ListNode:
    def __init__(self, x,next):
        self.val = x
        self.next = next


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
        def recurrent_iter(head, tail):
            if not head:
                return head
            slow, fast = head, head
            while fast:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            mid = slow

            right = mid.next
            mid.next = None
            return self.merge_sorted_list(recurrent_iter(head, mid), recurrent_iter(right, tail))

        return recurrent_iter(head, None)


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        pre = ListNode(0, head)
        self.quik_sort(pre, None)
        return pre.next

    def quik_sort(self, pre, end):
        if pre== end or pre.next ==end:
            return pre
        pivot = pre.next
        cur = ListNode(0, None)
        r: ListNode = pivot
        l = cur
        while r.next != end:
            if r.next.val <= pivot.val:
                l.next = r.next
                l = l.next
                r.next = r.next.next
            else:
                r = r.next
        l.next = pre.next
        pre.next = cur.next
        self.quik_sort(pivot, end)
        self.quik_sort(pre, pivot)
        #return pre.next



def recur_set(nums):
    pre = ListNode(0,None)
    n = pre
    for i in nums:
        nd = ListNode(i,None)
        n.next = nd
        n = n.next
    return pre.next

nd = recur_set([9,2,3,4,5])

k = Solution2().sortList(nd)
print(k)