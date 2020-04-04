package goal

// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

func countSmaller(nums []int) []int {
	stack := make([]int, 0)
	res := make([]int, len(nums))
	for idx := len(nums) - 1; idx >= 0; idx-- {
		if len(stack) == 0 {
			res[idx] = 0
			stack = append(stack, nums[idx])
			continue
		}
		if stack[len(stack)-1] < nums[idx] {
			res[idx] = stack[len(stack)-1]
			stack = append(stack, nums[idx])
			continue
		}
		for {
			top := len(stack) - 1
			if top < 0 || stack[top] < nums[idx] {
				if top == -1 {
					res[idx] = 0
					stack = append(stack, nums[idx])
					break
				}
				res[idx] = stack[top]
				stack = append(stack, nums[idx])
				break
			}
			stack = stack[:top]
		}

	}
	return res
}
