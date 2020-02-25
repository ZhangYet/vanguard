# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 我们的思路是对的，但是用递归来反转其实挺麻烦的。
class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start: ListNode = None
        cur: ListNode = head

        self.end = None
        def reverse(head:ListNode, step:int) -> ListNode:
            if step < 0:
                self.end = head.next
                return head

            new_head = reverse(head.next, step - 1)
            new_head.next = head
            head.next = None
            return new_head


        pos: int = 0
        while cur.next:
            if pos == 0:
                new_head = reverse(cur, m-n)
                if start:
                    start.next = new_head
                else:
                    head = new_head
                break

            start = cur if not start else cur
            cur = cur.next



        return head

