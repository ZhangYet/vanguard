package goal

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	var prev *ListNode = nil
	next := head.Next
	cur := head
	for {
		cur.Next = prev
		if next == nil {
			return cur
		}
		prev = cur
		cur = next
		next = next.Next
	}
}

func travelReverseList(head *ListNode) []int {
	res := []int{}
	for {
		if head == nil {
			return res
		}
		res = append(res, head.Val)
		head = head.Next
	}
}
