# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> Optional[TreeNode]:
        def dfs(root: TreeNode):
            if root is None:
                return None, 0
            left, l_val = dfs(root.left)
            right, r_val = dfs(root.right)
            check = root.val + l_val + r_val
            if l_val == 0:
                root.left = None
            if r_val == 0:
                root.right = None
            return root, check

        rt, check = dfs(root)

        if check == 0:
            return None

        return rt


rt = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
x = Solution().pruneTree(rt)
print(x.val)
