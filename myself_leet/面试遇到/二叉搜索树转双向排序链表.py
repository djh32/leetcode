# Definition for a binary tree node.
from typing import Optional

# 脉脉上看到别人的题目
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:

    def btree_to_st_node(self, root: Optional[TreeNode]) -> ListNode:
        self.pred = ListNode(None)
        self.tmp = self.pred
        def load(root):
            new_node = ListNode(root.val)
            self.tmp.next = new_node
            new_node.prev =  self.tmp
            self.tmp = new_node
        def dfs(root):  # 自下而上，比较恶心。 因为需要考虑none节点的取值范围。
            if not root:
                return None
            dfs(root.left)
            load(root)
            dfs(root.right)
        dfs(root)
        return self.pred.next

play_tree = TreeNode(7,TreeNode(5,TreeNode(1),TreeNode(6)),TreeNode(9,TreeNode(8),TreeNode(10)))

nd = Solution().btree_to_st_node(play_tree)
print(nd)


