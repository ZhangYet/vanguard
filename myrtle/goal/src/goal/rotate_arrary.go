package goal

// https://leetcode.com/problems/rotate-array/

func reverse(nums []int, start, end int) {
	for {
		if start >= end {
			break
		}
		nums[start], nums[end] = nums[end], nums[start]
		start += 1
		end -= 1
	}
}

func rotate(nums []int, k int) {
	k = k % len(nums)
	end := len(nums) - 1
	reverse(nums, 0, end)
	reverse(nums, 0, k-1)
	reverse(nums, k, end)
}
