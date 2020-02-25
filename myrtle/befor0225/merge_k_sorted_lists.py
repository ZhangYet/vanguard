from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def walk_and_find_min_node(lists: List[ListNode]) -> ListNode:
    min_node = lists[0]
    min_index = 0
    for i, listNode in enumerate(lists):
        if listNode is not None and (min_node is None or listNode.val < min_node.val):
            min_node = listNode
            min_index = i

    lists[min_index] = lists[min_index].next
    return min_node


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cur, res = None, None
        while any([l for l in lists]):
            min_node = walk_and_find_min_node(lists)
            if res is None:
                res = min_node
                cur = res
            else:
                cur.next = min_node
                cur = cur.next

        return res
