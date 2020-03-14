package goal

// https://leetcode.com/problems/missing-number/

func missingNumber(nums []int) int {
	l := len(nums)
	total := (l + 1) * l / 2
	pSum := 0
	for _, n := range nums {
		pSum += n
	}
	return total - pSum
}
