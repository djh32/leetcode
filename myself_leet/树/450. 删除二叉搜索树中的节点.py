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
