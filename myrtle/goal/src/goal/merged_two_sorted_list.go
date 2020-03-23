package goal

// https://leetcode.com/problems/merge-two-sorted-lists/
// 感觉没啥难度

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	dumpHead := &ListNode{Val: 0}
	head := dumpHead
	for {
		if l1 == nil && l2 == nil {
			break
		}
		if l1 == nil {
			head.Next = l2
			break
		}
		if l2 == nil {
			head.Next = l1
			break
		}
		if l1.Val < l2.Val {
			head.Next = l1
			l1 = l1.Next
		} else {
			head.Next = l2
			l2 = l2.Next
		}
		head = head.Next
	}
	return dumpHead.Next
}
