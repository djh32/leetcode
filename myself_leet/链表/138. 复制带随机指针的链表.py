"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        prev = Node(0)
        prev.next = head
        cur = head
        d = {}
        while cur != None:
            newNode = Node(cur.val)
            d[cur] = newNode
            cur = cur.next

        newPrev = Node(0)
        cur = prev.next
        newNode = d.get(cur)
        newPrev.next = newNode

        while cur != None:
            newNode = d[cur]
            newNode.next = d.get(cur.next, None)
            newNode.random = d.get(cur.random, None)
            cur = cur.next
        return newPrev.next

p = Node(0)
a = Node(1)
b = Node(2)
c = Node(3)

p.next = a
a.next = b
b.next = c
c.next = None

p.random = b
a.random = None
b.random = c
c.random = None

Solution().copyRandomList(p)
