# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        l,r = 0,len(nums)-1
        m = l+(r-l)//2
        nd = TreeNode(nums[m])
        nd.left = self.sortedArrayToBST(nums[:m])
        nd.right = self.sortedArrayToBST(nums[m+1:])
        return nd

n = Solution().sortedArrayToBST(list(range(8)))
print(n.val)