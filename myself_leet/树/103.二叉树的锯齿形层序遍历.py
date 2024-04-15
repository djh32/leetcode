#coding=utf-8
#103.二叉树的锯齿形层序遍历.py
# Definition for a binary tree node.
from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        i = 0
        l_to_r = [root]
        r_to_l = []
        res = []
        while l_to_r or r_to_l:
            now = []
            if i%2 == 0: #l to r
                for nd in l_to_r:
                    if nd is not None:
                        now.append(nd.val)
                        r_to_l.append(nd.left)
                        r_to_l.append(nd.right)
                l_to_r = []

            elif i%2 == 1: #r to l
                for nd in r_to_l:
                    if nd is not None:
                        now.append(nd.val)
                        l_to_r.append(nd.left)
                        l_to_r.append(nd.right)
                r_to_l = []
                now.reverse()
            if now:
                res.append(now)
            i += 1
        return res

from collections import deque
def zigzagLevelOrder2(root):
    tmp = deque([root])
    res = []

    cnt = 0
    while tmp:
        holder = len(tmp)
        now = []
        cnt +=1
        for i in range(holder):
            if tmp[0].left:
                tmp.append(tmp[0].left)
            if tmp[0].right:
                tmp.append(tmp[0].right)
            nd = tmp.popleft()
            now.append(nd.val)
        if cnt %2 ==0:
            now.reverse()

        res.extend(now)
    return res


def recur_make_tree(nums):
    if not nums: return None
    mid = len(nums)//2
    now = TreeNode(nums[mid])
    now.left = recur_make_tree(nums[:mid])
    now.right = recur_make_tree(nums[mid+1:])
    return now

t = recur_make_tree([1,2,3,4,5,6,7,8,9,1123,1,2,3])
t_r = zigzagLevelOrder2(t)
print(t_r)
#print(Solution().zigzagLevelOrder(t_r))

