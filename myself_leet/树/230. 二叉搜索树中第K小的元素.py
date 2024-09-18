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
                return False, None

            (left, lval) = dfs(root.left, cache)
            cache.append(root.val)
            if len(cache) == k:
                return True, root.val
            right, rval = dfs(root.right, cache)
            return (left, lval) if left else (right, rval)

        find, val = dfs(root, [])
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

        res = dfs(root, [])[-1]
        return res

    def play2(self, root: Optional[TreeNode], k: int) -> int:
        # 空间最优
        self.res = None
        self.have_seen = 0  # 必须用self，否则递归中seen为函数的初始变量

        def dfs(root, have_seen):
            if not root: return
            dfs(root.left, have_seen)
            self.have_seen += 1
            if self.have_seen == k:
                self.res = root.val
            if self.have_seen > k:
                return
            dfs(root.right, have_seen)

        dfs(root, 0)
        return self.res


demo_tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))

r = Solution().kthSmallest(demo_tree, 3)
r2 = Solution().play(demo_tree, 3)
r3 = Solution().play2(demo_tree, 3)
print(r, r2, r3)
