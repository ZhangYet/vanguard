package goal

func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	fast, slow := head, head
	flag := false
	for fast != nil {
		slow = slow.Next
		fast = fast.Next
		if fast == nil {
			return nil
		}
		fast = fast.Next
		if fast == slow {
			flag = true
			break
		}
	}
	if !flag {
		return nil
	}
	cur := head
	for cur != slow {
		cur = cur.Next
		slow = slow.Next
	}
	return cur
}
