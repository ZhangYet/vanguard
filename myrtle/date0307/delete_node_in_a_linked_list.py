# https://leetcode.com/problems/delete-node-in-a-linked-list/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 看《编程之美》学到的答案：找到 node 删除下一个 node，并把下一个 node 的值复制到当前 node


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next = node.next
        node.next = next.next
        node.val = next.val
        next.next = None
