package goal

import "container/heap"

// 用最大堆

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type KthLargest struct {
	heap *IntHeap
	K    int
}

func Constructor(k int, nums []int) KthLargest {
	h := &IntHeap{}
	heap.Init(h)
	for _, v := range nums {
		heap.Push(h, v)
	}
	for len(*h) > k {
		heap.Pop(h)
	}
	return KthLargest{heap: h, K: k}
}

func (this *KthLargest) Add(val int) int {
	if len(*this.heap) < this.K {
		heap.Push(this.heap, val)
	} else if val > (*this.heap)[0] {
		heap.Push(this.heap, val)
		heap.Pop(this.heap)
	}
	return (*this.heap)[0]
}
