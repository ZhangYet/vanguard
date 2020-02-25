# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ListNodeIterator(node: ListNode):
    while True:
        if not node:
            return
        yield node.val
        node = node.next



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(h: ListNode) -> ListNode:
            print(h.val)
            if not h.next:
                return h

            tail = reverse(h.next)
            tail.next = h
            h.next = None
            return h

        tail = head
        while tail.next:
            tail = tail.next
        reverse(head)
        return tail


def gen_case(n: int):
    n0 = ListNode(0)
    curr = n0
    for i in range(1, n):
        n = ListNode(i)
        curr.next = n
        curr = n
    return n0


def test_case():
    curr = gen_case(4)
    t = Solution()
    return t.reverseList(curr)
