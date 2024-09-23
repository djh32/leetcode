# Definition for a binary tree node.
from typing import List, Optional

"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return cur

            if cur.val > key:
                cur.left = dfs(cur.left)
            elif cur.val < key:
                cur.right = dfs(cur.right)
            else:  # cur.val == key
                if cur.left is None: return cur.right  # 这里就是删除当前节点了
                if cur.right is None: return cur.left
                # 左右都不为None
                # #f1找左子树最大值:
                # cur_iter_left = cur.left
                # while cur_iter_left.right:
                #     cur_iter_left = cur_iter_left.right
                # cur_iter_left.right = cur.right
                # return cur.left
                #f2找右子树最小值:
                cur_iter_right = cur.right
                while cur_iter_right.left:
                    cur_iter_right = cur_iter_right.left
                cur_iter_right.left = cur.left
                return cur.right
            return cur

        return dfs(root)


demo_tree = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))

r = Solution().deleteNode(demo_tree, 1)
print(r)
