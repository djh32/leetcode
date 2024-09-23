#coding=utf-8
"""
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。



你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]


提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(0,head)
        info_dict = {0:pre}
        pre_sum = 0
        while head is not None: # 虽然没问题但是没有技巧。
            pre_sum += head.val
            if pre_sum in info_dict:
                delete_nd = info_dict[pre_sum].next
                delete_pre_sum = pre_sum+delete_nd.val
                while delete_nd !=head:
                    info_dict.pop(delete_pre_sum)
                    delete_nd = delete_nd.next
                    delete_pre_sum += delete_nd.val
                info_dict[pre_sum].next = head.next
                head = head.next
            else:
                info_dict[pre_sum] = head  # mark
                head = head.next
        return pre.next

    def removeZeroSumSublists2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 相当精彩的题目
        info_dict = {}
        pre = ListNode(0,head)
        cur = pre
        sums =0
        while cur is not None:
            sums += cur.val
            info_dict[sums] = cur
            cur = cur.next
        cur = pre
        sums =0
        while cur is not None:
            sums += cur.val
            cur.next = info_dict[sums].next
            cur = cur.next
        return pre.next


l = [ListNode(v) for v in [1,2,3,4,5,-9,-3]]
for i in range(len(l)-1):
    l[i].next = l[i+1]
#l = Solution().removeZeroSumSublists(l[0])
l2 = Solution().removeZeroSumSublists2(l[0])

print(l2)

