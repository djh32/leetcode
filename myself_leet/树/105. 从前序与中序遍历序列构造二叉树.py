# Definition for a binary tree node.
from typing import List,Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]'''


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        m_idx = inorder.index(val)
        l = inorder[:m_idx]
        r = inorder[m_idx+1:]
        root.left = self.buildTree(preorder,l)
        root.right = self.buildTree(preorder,r)
        return root

r = Solution().buildTree(preorder = [3,9,20,15,7],inorder=[9,3,15,20,7])
print(r)