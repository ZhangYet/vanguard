# https://leetcode.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        fast, slow = head, head
        has_cycle = False
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                has_cycle = True
                break

        if not has_cycle:
            return None
        
        cur = head
        while cur != slow:
            cur = cur.next
            slow = slow.next

        return cur
