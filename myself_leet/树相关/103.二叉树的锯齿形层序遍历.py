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
r = TreeNode(3)
l1 = TreeNode(9)
l2 = TreeNode(20)
l3 = TreeNode(15)
l4 = TreeNode(7)
r.left = l1
r.right = l2
l2.right = l4
l2.left = l3

print(Solution().zigzagLevelOrder(r))

