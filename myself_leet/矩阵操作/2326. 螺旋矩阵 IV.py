import sys
from typing import List, Optional
"""

给你两个整数：m 和 n ，表示矩阵的维数。

另给你一个整数链表的头节点 head 。

请你生成一个大小为 m x n 的螺旋矩阵，矩阵包含链表中的所有整数。链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。如果还存在剩余的空格，则用 -1 填充。

返回生成的矩阵。



输入：m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
输出：[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
解释：上图展示了链表中的整数在矩阵中是如何排布的。
注意，矩阵中剩下的空格用 -1 填充。
示例 2：


输入：m = 1, n = 4, head = [0,1,2]
输出：[[0,1,2,-1]]
解释：上图展示了链表中的整数在矩阵中是如何从左到右排布的。 
注意，矩阵中剩下的空格用 -1 填充。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        now_r,now_c = 0,0
        l,r,t,b = 0,n,0,m
        res = [[0]*n for _ in range(m)]
        iter_num = 0
        need_find = m*n
        while iter_num < need_find:
            for i in range(l,r):
                now_c = i
                if head:
                    res[now_r][now_c] = head.val
                    head = head.next
                else:
                    res[now_r][now_c] = -1
                iter_num +=1
                if iter_num == need_find:return res

            t +=1
            for i in range(t,b):
                now_r = i
                if head:
                    res[now_r][now_c] = head.val
                    head = head.next
                else:
                    res[now_r][now_c] = -1
                iter_num +=1
                if iter_num == need_find: return res

            r -=1
            for i in range(r-1,l-1,-1):
                now_c = i
                if head:
                    res[now_r][now_c] = head.val
                    head = head.next
                else:
                    res[now_r][now_c] = -1
                iter_num +=1
                if iter_num == need_find: return res

            b -=1
            for i in range(b-1,t-1,-1):
                now_r = i
                if head:
                    res[now_r][now_c] = head.val
                    head = head.next
                else:
                    res[now_r][now_c] = -1
                iter_num +=1
                if iter_num == need_find: return res
            l +=1
        return res

m=4
n=6

nd_lst = [ListNode(v) for v in list(range(0,23))]

for i in range(1,23):
    nd_lst[i-1].next = nd_lst[i]

res = Solution().spiralMatrix(m,n,nd_lst[0])
for i in res:
    print(i)








