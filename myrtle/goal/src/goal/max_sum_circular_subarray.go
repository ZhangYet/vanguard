package goal

// 不能直接把两个 slice 拼在一起，然后按照 max sum subarray 的方法做
// 因为如果所有的数字都是正数，那我们会追尾
// 但是实践证明，这个解法是错误的

func maxSubarraySumCircular(A []int) int {
	ring := append(A, A...)
	curSum, maxSum := ring[0], ring[0]
	records := map[int]bool{0: true}
	for idx, num := range ring {
		if idx == 0 {
			continue
		}
		if _, ok := records[idx%len(A)]; ok {
			break
		}
		curSum += num
		if curSum < num { // 抛弃之前的记录
			records = map[int]bool{idx % len(A): true}
			curSum = num
		} else {
			records[idx%len(A)] = true
		}
		if curSum > maxSum {
			maxSum = curSum
		}
	}
	return maxSum
}
