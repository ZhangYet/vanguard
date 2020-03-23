package goal

import "fmt"

// https://leetcode.com/problems/remove-element/
// 还真的不好做（因为不能排序）
// 两次迭代，第一次标记 val 的座标，第二次从尾部开始，交换位置

func removeElement(nums []int, val int) int {
	pos := []int{}
	for idx, v := range nums {
		if v == val {
			pos = append(pos, idx)
		}
	}

	lPos, lNums := len(pos), len(nums)
	fmt.Printf("before swap pos: %v, nums: %v\n", pos, nums)
	res := lNums - lPos
	for i := lPos - 1; i >= 0; i-- {
		offset := lPos - i - 1
		toBeSwapIdx := lNums - offset - 1
		if pos[i] > toBeSwapIdx {
			continue
		}
		for {
			fmt.Printf("during swap pos: (%d, %d), toBeSwap: (%d, %d)\n", pos[i], nums[pos[i]], toBeSwapIdx, nums[toBeSwapIdx])
			if nums[toBeSwapIdx] != val {
				nums[toBeSwapIdx], nums[pos[i]] = nums[pos[i]], nums[toBeSwapIdx]
				break
			}
			toBeSwapIdx--
			if toBeSwapIdx < 0 {
				break
			}
		}
	}
	fmt.Printf("after swap pos: %v, nums: %v\n", pos, nums)
	return res
}
