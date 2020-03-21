package goal

// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
// 有个很妙的思路，因为 arr 是排好序的，所以我们只需要看当前元素跟列表长度四分之一之后的元素是否相等，就知道了

func findSpecialInteger(arr []int) int {
	gap := len(arr) / 4
	for i, num := range arr {
		if arr[i+gap] == num {
			return num
		}
	}
	return -1
}
