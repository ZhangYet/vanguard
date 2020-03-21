package goal

import (
	"math"
	"sort"
)

// https://leetcode.com/problems/minimum-absolute-difference/
// 这道题的妙处就在于将输入的 arr 排序，将复杂度从 n^2 降到 n

func minimumAbsDifference(arr []int) [][]int {
	if len(arr) <= 1 {
		return [][]int{}
	}
	sort.Ints(arr)
	records := make(map[int][][]int)
	minAbs := math.MaxInt32
	for i := 0; i < len(arr)-1; i++ {
		a := arr[i+1] - arr[i]
		if a <= minAbs {
			minAbs = a
			records[a] = append(records[a], []int{arr[i], arr[i+1]})
		}
	}
	return records[minAbs]
}
