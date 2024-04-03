# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root:TreeNode,deep:int):
            if not root:return
            if deep==len(res):
                res.append(root.val)
            else:
                res[deep] = root.val
            dfs(root.left, deep+1)
            dfs(root.right, deep +1)
        dfs(root,0)
        return res



