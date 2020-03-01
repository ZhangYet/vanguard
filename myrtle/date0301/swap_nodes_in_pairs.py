# https://leetcode.com/problems/swap-nodes-in-pairs/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy_node = ListNode(-1)
        first, second = head, head.next
        dummy_node.next = first
        zero = dummy_node

        while second:
            first.next = second.next
            second.next = first
            zero.next = second

            zero = first
            first = first.next
            if not first:
                break
            second = first.next

        return dummy_node.next


from typing import List


def construct_test_case(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    cur = head
    for n in nums[1:]:
        node = ListNode(n)
        cur.next = node
        cur = node
    return head


def test_case(nums: List[int]) -> List[int]:
    node = construct_test_case(nums)
    s = Solution()
    answer = s.swapPairs(node)
    res = []
    while answer:
        res.append(answer.val)
        answer = answer.next
    return res
