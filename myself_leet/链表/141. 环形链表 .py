# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = ListNode(None)
        slow = head
        if not head:
            return False
        fast = slow.next
        if not fast:
            return False
        while fast !=None and slow!=None:
            if fast == slow:
                return True
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next
            slow = slow.next
        return False