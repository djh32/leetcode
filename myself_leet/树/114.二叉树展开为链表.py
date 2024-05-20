#coding-utf-8
from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        rtn_root = root
        while root:
            if root.left:
                cache_left = root.left
                tmp_left = root.left
                right = root.right
                while tmp_left.right != None:
                    tmp_left = tmp_left.right
                tmp_left.right = right
                root.right =cache_left
                root.left = None
            root = root.right
        return rtn_root

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root ==None:
            return None
        # 纯trick的题
        while root:
            if root.left:
                tmp_left = root.left
                while tmp_left.right:
                    tmp_left = tmp_left.right
                tmp_left.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n5.right = n6

s = Solution().flatten(n1)
print (s)


