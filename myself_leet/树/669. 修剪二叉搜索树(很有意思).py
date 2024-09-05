# Definition for a binary tree node.
from typing import List, Optional

"""
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return cur

            if cur.val >= low and cur.val <= high:#对当前节点的判断
                cur.left = dfs(cur.left)
                cur.right = dfs(cur.right)
            else:
                if cur.val < low:
                    return dfs(cur.right) # 忽略当前节点，如果当前小于最小，那么往大方向走
                elif cur.val > high:
                    return dfs(cur.left)
            return cur
        return dfs(root)


demo_tree = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))

r = Solution().trimBST(demo_tree, 1, 1)
print(r)
