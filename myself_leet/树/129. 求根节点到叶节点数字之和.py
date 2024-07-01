# Definition for a binary tree node.
from typing import List, Optional

"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。
示例 1：


输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:  # 自己完成的回传记录
        def dfs(root) -> list:
            if not root:
                return []
            left = dfs(root.left)
            right = dfs(root.right)
            merge = [f"{root.val}{s}" for s in left + right] if left or right else [f"{root.val}"]
            return merge

        res = dfs(root)
        return sum([int(num) for num in res])

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # readme回答的，带入当前
        def dfs(root, current_val):
            if not root:
                return 0
            next_val = current_val * 10 + root.val
            if not root.left and not root.right: return next_val  # 两个子节点都没有的节点直接返回当前值，可以去掉跑跑看有助理解。
            left = dfs(root.left, next_val)
            right = dfs(root.right, next_val)
            return left + right

        res = dfs(root, 0)
        return res


demo_tree = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
# demo_tree = TreeNode(0, TreeNode(1))

print(Solution().sumNumbers(demo_tree))
