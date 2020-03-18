package goal

func maxSubArray(nums []int) int {
	if len(nums) < 1 {
		return 0
	}
	curSum, maxSum := nums[0], nums[0]
	for _, num := range nums[1:] {
		curSum += num
		if curSum < num {
			curSum = num
		}
		if maxSum < curSum {
			maxSum = curSum
		}
	}
	return maxSum
}
