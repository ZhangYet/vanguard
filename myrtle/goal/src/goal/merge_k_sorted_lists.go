package goal

import "math"

// 得写一个 struct 管理所有的节点
// 时间复杂度是列表数量乘以列表平均长度，比较慢

type noNilListNodeSet struct {
	lists []*ListNode
}

func (this *noNilListNodeSet) findMinIdx() int {
	idx := -1
	minimun := math.MaxInt32
	for i, node := range this.lists {
		if node.Val < minimun {
			idx = i
			minimun = node.Val
		}
	}
	return idx
}

func (this *noNilListNodeSet) stepForward(idx int) *ListNode {
	n := this.lists[idx]
	this.lists[idx] = this.lists[idx].Next
	if this.lists[idx] == nil {
		if len(this.lists) <= 1 {
			this.lists = nil
		} else if idx == 0 {
			this.lists = this.lists[1:]
		} else if idx == len(this.lists)-1 {
			this.lists = this.lists[:idx]
		} else {
			this.lists = append(this.lists[:idx], this.lists[idx+1:]...)
		}
	}
	return n
}

func (this *noNilListNodeSet) empty() bool {
	return this.lists == nil
}

func mergeKLists(lists []*ListNode) *ListNode {
	notNilLists := []*ListNode{}
	for _, list := range lists {
		if list != nil {
			notNilLists = append(notNilLists, list)
		}
	}
	if len(notNilLists) <= 0 {
		return nil
	}
	notNilSet := &noNilListNodeSet{lists: notNilLists}
	dump := &ListNode{Val: 0}
	head := dump
	for {
		minIdx := notNilSet.findMinIdx()
		node := notNilSet.stepForward(minIdx)
		head.Next = node
		head = head.Next
		if notNilSet.empty() {
			break
		}
	}
	return dump.Next
}
