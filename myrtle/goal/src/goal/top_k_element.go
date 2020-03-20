package goal

import "container/heap"

type kFreqItem struct {
	freq int
	val  int
}

type kFreqHeap []kFreqItem

func (h kFreqHeap) Len() int           { return len(h) }
func (h kFreqHeap) Less(i, j int) bool { return h[i].freq > h[j].freq }
func (h kFreqHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (this *kFreqHeap) Pop() interface{} {
	old := *this
	n := len(old)
	x := old[n-1]
	*this = old[0 : n-1]
	return x
}

func (this *kFreqHeap) Push(x interface{}) {
	*this = append(*this, x.(kFreqItem))
}

func topKFrequent(nums []int, k int) []int {
	freqCounter := make(map[int]int)
	for _, n := range nums {
		freqCounter[n] += 1
	}
	h := make(kFreqHeap, 0)
	heap.Init(&h)
	for val, freq := range freqCounter {
		item := kFreqItem{val: val, freq: freq}
		heap.Push(&h, item)
	}
	res := make([]int, k)
	for i := 0; i < k; i++ {
		item := heap.Pop(&h)
		res[i] = item.(kFreqItem).val
	}
	return res
}
