# Definition for a binary tree node.
from typing import List, Optional

"""
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
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



demo_tree = TreeNode(5, TreeNode(3, TreeNode(2,TreeNode(1)), TreeNode(4)), TreeNode(6))

r = Solution().kthSmallest(demo_tree, 3)
print(r)
