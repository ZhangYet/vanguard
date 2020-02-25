# https://leetcode.com/problems/linked-list-cycle/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast, slow = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
            if fast == slow:
                return True

        return False
