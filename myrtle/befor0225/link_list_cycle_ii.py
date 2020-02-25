# https://leetcode.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head
        fast, slow = head, head
        flag = False
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
            if fast == slow:
                flag = True

        if not flag:
            return None

        cur = head
        while cur != slow:
            cur = cur.next
            slow = slow.next

        return cur
