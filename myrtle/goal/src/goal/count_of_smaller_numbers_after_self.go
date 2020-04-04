package goal

// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

func countsmaller(nums []int, target int) int {
	res := 0
	for _, num := range nums {
		if num < target {
			res += 1
		}
	}
	return res
}

func countSmaller(nums []int) []int {
	if len(nums) <= 0 {
		return []int{}
	}
	res := make([]int, len(nums))
	end := len(nums) - 1
	res[end] = 0
	for idx := len(nums) - 2; idx >= 0; idx-- {
		res[idx] = countsmaller(nums[idx:], nums[idx])
	}
	return res
}
