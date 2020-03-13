# https://leetcode.com/problems/next-greater-node-in-linked-list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        elems = []
        while head:
            elems.append(head.val)
            head = head.next

        res = [0] * len(elems)
        from collections import deque
        stack = deque()  # stack 保存当前没有找到 next greater 的元素的座标

        for i in range(len(elems)):
            while stack and elems[stack[-1]] < elems[i]:
                res[stack[-1]] = elems[i]
                stack.pop()
            stack.append(i)
        return res
