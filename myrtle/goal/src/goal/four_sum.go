package goal

import "sort"

// https://leetcode.com/problems/4sum/
// 排序然后剪枝
func fourSum(nums []int, target int) [][]int {
	var res [][]int
	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		for j := i + 1; j < len(nums); j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			k := j + 1
			l := len(nums) - 1

			for k < l {
				if k > j+1 && nums[k] == nums[k-1] {
					k++
					continue
				}
				if l < len(nums)-1 && nums[l] == nums[l+1] {
					l--
					continue
				}
				sum := nums[i] + nums[j] + nums[k] + nums[l]
				if sum == target {
					temp := []int{nums[i], nums[j], nums[k], nums[l]}
					res = append(res, temp)
					k++
					l--
				} else if sum < target {
					k++
				} else {
					l--
				}
			}
		}
	}
	return res
}
