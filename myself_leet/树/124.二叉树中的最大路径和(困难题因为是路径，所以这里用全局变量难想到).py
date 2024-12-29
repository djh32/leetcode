# coding=utf-8
"""

二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。


"""
class TreeNode():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def __init__(self):
        self.max_holder = 0

    # def process(self,root):
    #     self.get_max_sum_from_tree(root)
    #     return self.max_holder
    def maxPathSum(self, root):
        def helper(root):
            if not root:
                return 0
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            self.max_holder = max(self.max_holder, left_sum + right_sum + root.val)
            max_num = max(root.val, max(left_sum, right_sum) + root.val)
            return max_num
        helper(root)
        return self.max_holder

class Solution2:
    ans = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            self.ans = max(self.ans, max(l,0) + max(r, 0) + node.val) #必须选择root 同时选择子节点大的+根val和存储值比大
            return max(l, r, 0) + node.val
        helper(root)
        return self.ans
#
# 输入：[-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# 输出：42

rt = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(Solution().maxPathSum(rt))
