package goal

// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
// 从右边开始扫起，用 stack 保存最大的值
func replaceElements(arr []int) []int {
	stack := []int{}
	for i := len(arr) - 1; i >= 0; i-- {
		v := arr[i]
		if len(stack) <= 0 {
			stack = append(stack, v)
			arr[i] = -1
			continue
		}
		replacement := stack[len(stack)-1]
		if v > replacement {
			stack = append(stack, v)
		}
		arr[i] = replacement
	}
	return arr
}
