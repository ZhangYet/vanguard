package goal

// https://leetcode.com/problems/single-number-ii/
// 因为其他数字重复三次，所以异或不能用

func singleNumber(nums []int) int {
	records := make(map[int]int)
	for _, num := range nums {
		if _, ok := records[num]; ok {
			records[num] += 1
		} else {
			records[num] = 1
		}
	}
	for k, v := range records {
		if v == 1 {
			return k
		}
	}
	return -1
}
