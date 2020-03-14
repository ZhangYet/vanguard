package goal

// 尝试用堆

type freqItem struct {
	val  int
	freq int
}

type freqHeap []freqItem

func (this freqHeap) Len() int {
	return len(this)
}

func (this freqHeap) Less(i, j int) bool {
	return this[i].freq < this[j].freq
}

func (this freqHeap) Swap(i, j int) {
	this[i], this[j] = this[j], this[i]
}

func (this *freqHeap) Push(x interface{}) {
	*this = append(*this, x.(freqItem))
}

func (this *freqHeap) Pop() interface{} {
	old := *this
	n := len(old)
	x := old[n-1]
	*this = old[0 : n-1]
	return x
}

func majorityElement(nums []int) int {
	counter := make(map[int]int)
	for _, num := range nums {
		counter[num] += 1
	}
	res, f := 0, 0
	for val, freq := range counter {
		if freq > f {
			res = val
			f = freq
		}
	}
	return res
}
