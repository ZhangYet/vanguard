package goal

import (
	"container/heap"
	"fmt"
)

// 直接算子树的和
// 最后用一个最大堆找 most freq
// 对 go 的 heap 还是不熟啊。（记得 Less 取 > 可以获得最大堆）
// heap 的 pop 会把堆顶元素放到尾部，然后我们的 Pop() 要把最后的元素取出来

type treeFreqItem struct {
	val  int
	freq int
}

type treeFreqHeap []treeFreqItem

func (this treeFreqHeap) Len() int {
	return len(this)
}

func (this treeFreqHeap) Less(i, j int) bool {
	return this[i].freq > this[j].freq
}

func (this treeFreqHeap) Swap(i, j int) {
	this[i], this[j] = this[j], this[i]
}

func (this *treeFreqHeap) Push(x interface{}) {
	*this = append(*this, x.(treeFreqItem))
}

func (this *treeFreqHeap) Pop() interface{} {
	old := *this
	n := len(old)
	x := old[n-1]
	*this = old[0 : n-1]
	return x
}

func (this *treeFreqHeap) output() {
	fmt.Printf("len of h : %d\n", len(*this))
	for _, item := range *this {
		fmt.Printf("(%d, %v) ", item.val, item.freq)
	}
	fmt.Printf("\n")
	return
}

var sumRecords map[int]int

func sumTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	curSum := root.Val + sumTree(root.Left) + sumTree(root.Right)
	if _, ok := sumRecords[curSum]; ok {
		sumRecords[curSum] += 1
	} else {
		sumRecords[curSum] = 1
	}
	return curSum
}

func findFrequentTreeSum(root *TreeNode) []int {
	sumRecords = make(map[int]int)
	sumTree(root)
	h := treeFreqHeap{}
	heap.Init(&h)
	for val, freq := range sumRecords {
		item := treeFreqItem{
			val:  val,
			freq: freq,
		}
		heap.Push(&h, item)
	}
	itemRes := []treeFreqItem{}
	maxFreq := 0
	iterLoop := len(h)
	for i := 0; i < iterLoop; i++ {
		item := heap.Pop(&h).(treeFreqItem)
		if item.freq < maxFreq {
			break
		}
		maxFreq = item.freq
		itemRes = append(itemRes, item)
	}

	res := make([]int, len(itemRes))
	for i, v := range itemRes {
		res[i] = v.val
	}
	return res
}
