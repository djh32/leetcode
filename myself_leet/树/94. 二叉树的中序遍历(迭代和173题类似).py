# Definition for a binary tree node.
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            while stack:
                if stack[-1].right !=None:
                    break
                res.append(stack.pop().val)
            if not stack:
                return res
            new_node = stack.pop()
            res.append(new_node.val)
            cur = new_node.right
        return res

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = []
        ans = []
        cur = root

        while cur or stack: # 优雅。
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
rt = TreeNode(2,TreeNode(1),TreeNode(3,TreeNode(4,TreeNode(5),TreeNode(6))))
print(Solution().inorderTraversal(rt))

