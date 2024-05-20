# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 很有意思的题目，如果只用两边的深度相加那么获取不到真正的最长长度，不能只考虑root节点，因为最大的结果可能在下面的子节点作为root的答案里面
class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.get_height(root)
        return self.max


    def get_height(self,root):
        if not root:
            return 0
        l_h = self.get_height(root.left)
        r_h = self.get_height(root.right)
        self.max = max(l_h + r_h,self.max)
        return max(l_h,r_h) + 1
