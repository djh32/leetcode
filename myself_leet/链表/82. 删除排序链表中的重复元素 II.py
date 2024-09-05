#coding=utf-8
"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        begin,n1 = dummy,dummy.next
        delete = False
        while n1:
            n2 = n1.next
            while n2 and n2.val == n1.val:
                n2 = n2.next
                delete = True
            if delete:
                begin.next = n2
                n1 = begin.next
                delete = False
            else:
                begin = begin.next # or n1
                n1 = begin.next
        return dummy.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val: # 一直删除
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

in_array = [1,1,1,2,3]
nd_list =[ListNode(x) for x in in_array]
for i in range(len(in_array)-1):
    nd_list[i].next = nd_list[i+1]

nd = Solution().deleteDuplicates(nd_list[0])
print (nd)






