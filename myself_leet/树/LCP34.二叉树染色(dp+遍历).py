# coding-utf-8
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxValue(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root) -> List[int]:
            layer_dp = [0] * (k+1)
            if root is None:
                return layer_dp
            left_dp = dfs(root.left)
            right_dp = dfs(root.right)

            # 当前root不染色:
            layer_dp[0] = max(left_dp) + max(right_dp)

            # 当前root染色
            for i in range(1,k+1):
                tmp = [0] * (i+1)
                for j in range(i):
                    tmp[i] = max(left_dp[j] + right_dp[i-1-j],tmp[i])
                layer_dp[i] = max(tmp) + root.val
            return layer_dp
        return max(dfs(root))

t = TreeNode(5,TreeNode(2,TreeNode(4)),TreeNode(3))
print(Solution().maxValue(t,2))

