# coding=utf-8

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
