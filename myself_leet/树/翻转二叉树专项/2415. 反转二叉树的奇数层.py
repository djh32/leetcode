#coding=utf-8
from typing import List,Optional
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
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
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(root1,root2,need_reverse):
            if not root1:
                return
            if need_reverse:
                root1.val,root2.val = root2.val,root1.val
            dfs(root1.left,root2.right,not need_reverse)
            dfs(root1.right,root2.left,not need_reverse)
        dfs(root.left,root.right,True)
        return root


nd = Solution().buildTree([1,2,4,8,9,5,10,11,3,8,6,7,7,4,2],[8,4,9,2,10,5,11,1,6,8,7,3,4,7,2])
Solution().reverseOddLevels(nd)
print(nd.val)










