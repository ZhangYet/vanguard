package goal

// https://leetcode.com/problems/remove-element/
// 还真的不好做（因为不能排序）
// 两次迭代，第一次标记 val 的座标，第二次从尾部开始，交换位置

func removeElement(nums []int, val int) int {
	finalLen := 0
	for _, num := range nums {
		if num != val {
			nums[finalLen] = num
			finalLen++
		}
	}
	return finalLen
}
