# coding=utf-8

from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge_sort(h1: ListNode, h2: ListNode) -> ListNode:
            h = res = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    h.next = h1
                    h1 = h1.next
                else:
                    h.next = h2
                    h2 = h2.next
                h = h.next
            h.next = h1 if h1 else h2
            return res.next

        def dfs_merge(lists: List[ListNode]) -> ListNode:
            if len(lists) == 1:
                return lists[0]
            mid = len(lists) // 2
            left = dfs_merge(lists[:mid])
            right = dfs_merge(lists[mid:])
            merge_nd = merge_sort(left, right)
            return merge_nd

        res = dfs_merge(lists)
        return res

def recur_set(nums):
    pre = ListNode(0, None)
    n = pre
    for i in nums:
        nd = ListNode(i, None)
        n.next = nd
        n = n.next
    return pre.next


nd = recur_set([1, 4,5])
nd2 = recur_set([1, 3, 4])
nd3 = recur_set([2, 6])

#t = Solution().mergeKLists([nd,nd2])
k = Solution().mergeKLists([[]])
print(k)
