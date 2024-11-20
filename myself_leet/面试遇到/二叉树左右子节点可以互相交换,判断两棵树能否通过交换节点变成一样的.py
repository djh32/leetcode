# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def change_same(self,t1,t2):
        q1 = deque([t1])
        q2 = deque([t2])
        while q1 or q2:
            p1 = q1.popleft()
            p2 = q2.popleft()
            #if p1 == p2 == None:continue
            if set([p1.left.val if p1.left else None,p1.right.val if p1.right else None]) == set([p2.left.val if p2.left else None,p2.right.val if p2.right else None]):
                q1.extend(filter(lambda x:x is not None , [p1.left,p1.right])) # None不能入遍历 会乱。
                q2.extend(filter(lambda x:x is not None , [p2.left,p2.right]))
            else:
                return False
        return True


t1 = TreeNode(1,TreeNode(2),TreeNode(3,None,TreeNode(5)))
t2 = TreeNode(1,TreeNode(3),TreeNode(2,TreeNode(5),None))

print(Solution().change_same(t1,t2))










