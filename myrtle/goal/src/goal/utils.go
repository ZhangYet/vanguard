package goal

import "reflect"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (this *ListNode) ToSlice() []int {
	res := []int{}
	head := this
	for {
		if head == nil {
			break
		}
		res = append(res, head.Val)
		head = head.Next
	}
	return res
}

func GenListNodeFromSlice(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	h := &ListNode{Val: nums[0]}
	cur := h
	for _, n := range nums[1:] {
		tmp := &ListNode{Val: n}
		cur.Next = tmp
		cur = tmp
	}
	return h
}

func CompareList(l1 *ListNode, l2 *ListNode) bool {
	nums1, nums2 := l1.ToSlice(), l2.ToSlice()
	return reflect.DeepEqual(nums1, nums2)
}
