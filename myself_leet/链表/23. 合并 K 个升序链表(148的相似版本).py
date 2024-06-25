#coding=utf-8

from typing import List,Optional
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_sort(lists)
        def dfs_merge(lists: List[ListNode]):
            if len(lists) == 1:
                return lists
            mid = len(lists)//2
            left = dfs_merge(lists[:mid])
            right = dfs_merge(lists[mid:])
            merged = merge_sort(left,right)





def recur_set(nums):
    pre = ListNode(0, None)
    n = pre
    for i in nums:
        nd = ListNode(i, None)
        n.next = nd
        n = n.next
    return pre.next


nd = recur_set([1,2,3])
nd2 = recur_set([4,5,87])
nd3 = recur_set([41,15])

k = Solution().mergeKLists([nd,nd2,nd3])
print(k)
