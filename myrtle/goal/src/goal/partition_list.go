package goal

import "fmt"

// https://leetcode.com/problems/partition-list/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// 感觉很简单，两条链就好
func partition(head *ListNode, x int) *ListNode {
	largerList := &ListNode{Val: 0}
	smallerList := &ListNode{Val: 0}
	largerHead, smallerHead := largerList, smallerList
	cur := head
	for {
		if cur == nil {
			break
		}
		fmt.Printf("dead loop here?\n")
		if cur.Val >= x {
			largerHead.Next = &ListNode{Val: cur.Val}
			largerHead = largerHead.Next
		} else {
			smallerHead.Next = &ListNode{Val: cur.Val}
			smallerHead = smallerHead.Next
		}
		cur = cur.Next
	}
	// find tail
	prev := smallerList
	for {
		if prev.Next == nil {
			prev.Next = largerList.Next
			return smallerList.Next
		}
		prev = prev.Next
	}
}
