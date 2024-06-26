# coding=utf-8

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root:
                return root
            if root.val > p.val and root.val > q.val:
                return dfs(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return dfs(root.right,p,q)
            return root
        return dfs(root,p,q)


