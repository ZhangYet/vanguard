package goal

// TODO

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	index := 1
	prev := head
	for {
		if index < m {
			prev = prev.Next
			continue
		}
		cur := prev.Next
		next := cur.Next
		for {
			cur.Next = prev
			if index >= n {
				break
			}
			prev = cur
			cur = next
			next = next.Next
		}
		return head
	}
}
