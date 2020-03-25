package goal

// 要求时间 O(n lg n) 空间复杂度常数。
// 用 merge sort, 这样空间只需要两个额外的空间放 list node
// 累了，不想做了

func sortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	var size int = 0
	cur := head
	for {
		if cur == nil {
			break
		}
		size++
		cur = cur.Next
	}
	dump := &ListNode{Val: -1}
	dump.Next = head
	for i := 1; i < size; i *= 2 {
		cur := dump.Next
		trace := dump
		for {
			if cur == nil {
				break
			}
			cur1 := cur
			cur2 := cut(i, cur)
			trace.Next = merge(cur1, cur2)
			for {
				if trace != nil && trace.Next != nil {
					trace = trace.Next
				}
			}
		}
	}
	return dump.Next
}

func cut(num int, head *ListNode) *ListNode {
	cur := head

	for {
		if num > 0 && cur != nil {
			cur = cur.Next
		}
		break
	}
	if cur == nil {
		return nil
	}
	next := cur.Next
	cur.Next = nil
	return next
}

func merge(head1, head2 *ListNode) *ListNode {
	left, right := head1, head2
	dump := &ListNode{Val: -1}
	begin := dump

	for {
		if left == nil || right == nil {
			break
		}
		if left.Val < right.Val {
			begin.Next = left
			left = left.Next
		} else {
			begin.Next = right
			right = right.Next
		}
		begin = begin.Next
	}
	if left != nil {
		begin.Next = left
	}
	if right != nil {
		begin.Next = right
	}
	return dump.Next
}
