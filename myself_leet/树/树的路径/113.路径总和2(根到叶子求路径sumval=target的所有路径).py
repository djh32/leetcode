# coding=utf-8
from typing import Optional, List

"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root, path: List[int]):
            if not root:
                return None
            if sum(path) > targetSum:
                return None

            path.append(root.val)
            if sum(path) == targetSum:
                result.append(path.copy())
                path.pop(-1)
                return
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop(-1)

        dfs(root, [])
        return result

rt = TreeNode(1, TreeNode(2,TreeNode(4),TreeNode(5)), TreeNode(3))
print(Solution().pathSum(rt,8))