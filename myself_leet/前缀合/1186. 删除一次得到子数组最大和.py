#coding=utf-8
"""
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
注意，删除一个元素后，子数组 不能为空。

示例 1：

输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
示例 2：

输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。
示例 3：

输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。

提示：

1 <= arr.length <= 105
-104 <= arr[i] <= 104
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

