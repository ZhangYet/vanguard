# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# 有序这个特性不知道怎样利用。
# 难点在于所有重复的项都需要被删除，同时 head 节点有可能会被删除。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head  # 用一个 dummy_head 记录 head， 最后返回 dummy_head.next
        prev, first, second = dummy_head, head, head.next

        find_dup = False
        while first and second:  # trival 的情况就是只有一个节点，这个循环条件可以处理这种情况
            while second and first.val == second.val:  # 出现需要删除的情况
                second = second.next
                find_dup = True

            if find_dup:
                prev.next = second
                first = second
                if first:
                    second = first.next
                find_dup = False
                continue

            prev = prev.next
            first = first.next
            second = second.next

        return dummy_head.next


# 总结：其实不难，就是难处理边界条件。保持一个不变量会简单一点。
