package goal

// https://leetcode.com/problems/reorder-list/submissions/ 有空改进一下
func reorderList(head *ListNode) {
	cur := head
	if cur == nil {
		return
	}
	if cur.Next == nil {
		return
	}
	reorderListHead(cur)
	cur = cur.Next.Next
	for cur != nil {
		reorderListHead(cur)
		if cur.Next == nil {
			break
		}
		cur = cur.Next.Next
	}

	return
}

func reorderListHead(head *ListNode) {
	if head.Next == nil {
		return
	}
	beforeTail, tail := head, head.Next
	if tail.Next == nil {
		return // 只有两个节点的平凡情况
	}
	for tail.Next != nil {
		tail = tail.Next
		beforeTail = beforeTail.Next
	}
	beforeTail.Next = nil
	tail.Next = head.Next
	head.Next = tail
	return
}
