#coding=utf-8
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.deque = []
        self.dfsTest(self.root)


    def dfsTest(self, root: Optional[TreeNode]):
        if root is not None:
            self.deque.append(root)
            self.dfsTest(root.left)
    def next(self) -> int:

        tail = self.deque.pop()
        tail_right = tail.right

        self.dfsTest(tail_right)

        return tail.val

    def hasNext(self) -> bool:
        return True if len(self.deque) >0 else False


rt = TreeNode(7,TreeNode(3),TreeNode(10,TreeNode(8,None,TreeNode(9)),TreeNode(12)))
iter = BSTIterator(rt)
print(iter.hasNext())
print(iter.next())
print(iter.next())
print(iter.next())
print(iter.next())
print(iter.next())
print(iter.next())
print(iter.hasNext())

