package goal

// https://leetcode.com/problems/next-greater-element-ii/
// 栈里面保存比栈顶小的元素的 i， 后面每个元素先比较栈顶

type simpleStack []int

func (this *simpleStack) push(num int) {
	*this = append(*this, num)
}

func (this *simpleStack) pop() int {
	n := len(*this)
	res := (*this)[n-1]
	*this = (*this)[0 : n-1]
	return res
}

func (this *simpleStack) notEmpty() bool {
	return len(*this) > 0
}

func (this *simpleStack) top() int {
	return (*this)[len(*this)-1]
}

func nextGreaterElements(nums []int) []int {
	l := len(nums)
	ring := append(nums, nums...)
	stack := make(simpleStack, 0)
	res := make([]int, l)
	for i := range res {
		res[i] = -1
	}
	for i, num := range ring {
		for {
			if stack.notEmpty() && nums[stack.top()%l] < num {
				index := stack.pop()
				res[index%l] = num
			} else {
				break
			}
		}
		stack.push(i)
	}
	return res
}
