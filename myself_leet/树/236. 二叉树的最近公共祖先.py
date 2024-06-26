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

            lefts = dfs(root.left, p, q)
            rights = dfs(root.right, p, q)

            if root == p or root == q:
                return root
            if lefts and rights:
                return root
            if lefts or rights:
                return lefts if lefts else rights

        return dfs(root,p,q)




