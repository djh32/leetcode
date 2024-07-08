# Definition for a binary tree node.
from typing import List, Optional

"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, cache: List):
            if not root:
                return False,None

            (left,lval) = dfs(root.left, cache)
            cache.append(root.val)
            if len(cache) == k:
                return True,root.val
            right,rval = dfs(root.right, cache)
            return (left,lval) if left else (right,rval)
        find,val = dfs(root,[])
        return val

    def play(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, cache: List):
            if not root or len(cache) == k:
                return
            dfs(root.left, cache)
            if k > len(cache):
                cache.append(root.val)
            dfs(root.right, cache)
            return cache
        res = dfs(root,[])[-1]
        return res




demo_tree = TreeNode(5, TreeNode(3, TreeNode(2,TreeNode(1)), TreeNode(4)), TreeNode(6))

r = Solution().kthSmallest(demo_tree, 3)
r2 = Solution().play(demo_tree, 3)

print(r,r2)
