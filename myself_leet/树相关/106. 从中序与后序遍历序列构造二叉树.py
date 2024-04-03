# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        val = postorder.pop(-1)
        root = TreeNode(val)
        m_idx = inorder.index(val)
        l = inorder[:m_idx]
        r = inorder[m_idx+1:]
        root.right = self.buildTree(r,postorder)
        root.left = self.buildTree(l,postorder)

        return root

r = Solution().buildTree(inorder = [9,3,15,20,7],postorder = [9,15,7,20,3])
print(r)