# coding=utf-8
# 103.二叉树的锯齿形层序遍历.py
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if l is None and r is None:
                return True
            if l.val != r.val:
                return False
            if (l is None and r is not None) or (r is None and l is not None):
                return False
            test1 = dfs(l.left, r.right)
            test2 = dfs(l.right, r.left)
            return test1 and test2

        return dfs(root.left, root.right)



t = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1123, 1, 2, 3])
t_r = Solution().isSymmetric(t)
print(t_r)
