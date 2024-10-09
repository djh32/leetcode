# Definition for a binary tree node.
from typing import Optional

"""
给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
示例 1：

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree_Error(self, root: Optional[TreeNode]) -> None:

        """
        Do not return anything, modify root in-place instead.
        """
        self.x, self.y = None, None

        def dfs(cur, pre):
            # 自己写的，只能过个例。 pre初始化的时候有问题，pre第一次赋值需要找到在遍历最左边节点的时候。
            # 可以过 rt = TreeNode(2, TreeNode(1, None, TreeNode(3)),None)
            if not cur:
                return pre

            pre = dfs(cur.left, pre)
            now_val = cur.val

            if pre is not None and pre.val > now_val:
                if self.x is not None:
                    self.y = cur
                else:
                    self.x, self.y = pre, cur

            dfs(cur.right, cur)
            return cur

        r = dfs(root, None)
        if self.x is not None and self.y is not None:
            self.x.val, self.y.val = self.y.val, self.x.val
        return r

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.x, self.y, self.pre = None, None, None

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 中序遍历到最左
            if not self.pre:
                self.pre = cur  # 最左节点初始化
            else:
                if cur.val < self.pre.val:
                    if not self.x and not self.y:
                        self.x, self.y = self.pre, cur
                    elif self.x is not None:
                        self.y = cur
                self.pre = cur
            dfs(cur.right)
            return cur

        r = dfs(root)
        if self.x is not None and self.y is not None:
            self.x.val, self.y.val = self.y.val, self.x.val
        return r
    def recoverTree2(self,root: Optional[TreeNode]): # O(n)的空间复杂度， 因为需要临时存储node后面交换。不如上面的是最优
        self.tmp_nd_holder = []
        def dfs(rt:TreeNode):
            if not rt:
                return
            dfs(rt.left)
            self.tmp_nd_holder.append(rt)
            dfs(rt.right)

        dfs(root)
        print([x.val for x in self.tmp_nd_holder])
        self.x,self.y = None,None
        for i in range(1,len(self.tmp_nd_holder)):
            if self.tmp_nd_holder[i-1].val>self.tmp_nd_holder[i].val:
                if not self.x and not self.y:
                    self.x = self.tmp_nd_holder[i-1]
                    self.y = self.tmp_nd_holder[i]
                elif self.x:
                    self.y = self.tmp_nd_holder[i]
        if self.x:
            self.x.val,self.y.val = self.y.val,self.x.val
        print([x.val for x in self.tmp_nd_holder])
        return root


# rt = TreeNode(7, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, TreeNode(6), TreeNode(4)))
rt = TreeNode(2, TreeNode(1, None, TreeNode(3)), None)
r = Solution().recoverTree(rt)
print(r)
