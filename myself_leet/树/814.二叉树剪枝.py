# Definition for a binary tree node.
from typing import List, Optional

"""
给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。
返回移除了所有不包含 1 的子树的原二叉树。
节点 node 的子树为 node 本身加上所有 node 的后代。
"""


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

    def review(self, root: TreeNode) -> Optional[TreeNode]: # play的记录，不如上述按照sumadd作为判断简介，比较啰嗦。
        def dfs(root) -> (TreeNode, bool):
            if not root: return None, True
            l, lc = dfs(root.left)
            r, rc = dfs(root.right)
            if root.val == 0:
                if lc and rc:
                    return root, True
                elif lc:
                    root.left = None
                    return root, False
                elif rc:
                    root.right = None
                    return root, False

            if root.val == 1:
                if lc: root.left = None
                if rc: root.right = None
            return root, False

        rt, root_check = dfs(root)

        return rt if root_check==False else None


# rt = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
rt = TreeNode(0, None, TreeNode(0, TreeNode(0), TreeNode(0)))

x = Solution().review(rt)
print(x.val)
