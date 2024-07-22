# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):  # 自下而上，比较恶心。 因为需要考虑none节点的取值范围。
            if not root:
                return True, float("-inf"), float("inf")
            left_good, left_max, left_min = dfs(root.left)
            right_good, right_max, right_min = dfs(root.right)
            good = left_good and right_good and left_max < root.val and root.val < right_min
            maxinfo = max(root.val, left_max, right_max)
            mininfo = min(root.val, left_min, right_min)

            return good, maxinfo, mininfo

        return dfs(root)[0]

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        l, r = float('-inf'), float('inf')

        def dfs(root, l, r):
            if not root:
                return True
            # 自上而下，从跟节点考虑，拆分区间
            if not l < root.val < r:
                return False
            left_part = [l, root.val]
            right_part = [root.val, r]
            left_res = dfs(root.left, left_part[0], left_part[1])
            right_res = dfs(root.right, right_part[0], right_part[1])
            return left_res and right_res

        return dfs(root, l, r)


rt = TreeNode(2, TreeNode(1), TreeNode(3))
x = Solution().isValidBST(rt)
y = Solution().isValidBST2(rt)

print(x, y)
