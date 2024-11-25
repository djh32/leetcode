# Definition for singly-linked list.
from typing import Optional

"""
143. 重排链表
中等
相关标签
相关企业
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def ret_middle(self,nd:ListNode):
        s = nd
        if not s:
            return s
        f = nd.next
        while f:
            s = s.next
            for _ in range(2):
                f = f.next
                if not f:
                    return s
                #f = f.next
        return s
    def getMidNode(self,head):
        dummy = ListNode(0)
        dummy.next = head
        slow,fast = dummy,dummy
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self,nd:ListNode):
        def recur(nd,nd_next):
            if nd.next == None:
                return nd
            first = recur(nd.next,nd.next.next)
            nd_next.next = nd
            return first
        fst = recur(nd,nd.next)
        nd.next = None # first origin
        return fst

    def limit_nd_list(self,nd):
        mid = self.ret_middle(nd)
        tail = self.reverse(mid.next)
        head = nd
        pass




nd_ls = [ListNode(x) for x in [1,2,3,4,5,6,7]]
for i in range(len(nd_ls)-1):
    nd_ls[i].next = nd_ls[i+1]

m1 = Solution().getMidNode(nd_ls[0])
m2 = Solution().ret_middle(nd_ls[0])

nd1 = Solution().limit_nd_list(nd_ls[0])
print(nd1)



