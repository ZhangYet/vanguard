package goal

import (
	"fmt"
	"math"
)

// https://leetcode.com/problems/missing-number/

func abs(i int) int {
	if i >= 0 {
		return i
	}
	return -i
}

func missingNumber(nums []int) int {
	l := len(nums)
	nums = append(nums, math.MaxInt32)
	for _, num := range nums[:l] {
		index := abs(num)
		if index == math.MaxInt32 {
			index = 0
		}
		if nums[index] > 0 {
			nums[index] = -nums[index]
		}
		if nums[index] == 0 {
			nums[index] = -math.MaxInt32
		}
	}
	for k, v := range nums {
		if v >= 0 {
			return k
		}
	}
	return 0
}
