package goal

type myStack struct {
	data []int
}

func (this *myStack) append(val int) {
	this.data = append(this.data, val)
}

func (this *myStack) notEmpty() bool {
	return len(this.data) > 0
}

func (this *myStack) pop() int {
	res := this.data[len(this.data)-1]
	this.data = this.data[:len(this.data)-1]
	return res
}

func newMyStack() *myStack {
	return &myStack{
		data: make([]int, 0),
	}
}

func longestValidParentheses(s string) int {
	stack := newMyStack()
	index := make([]int, len(s))
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack.append(i)
			continue
		}
		if s[i] == ')' && stack.notEmpty() {
			index[i] = 1
			tmp := stack.pop()
			index[tmp] = 1
		}

	}

	res := make([]int, 0)
	tmp := 0
	for _, v := range index {
		if v == 1 {
			tmp += 1
		} else {
			if tmp > 0 {
				res = append(res, tmp)
				tmp = 0
			}
		}
	}
	if tmp > 0 {
		res = append(res, tmp)
	}

	if len(res) > 0 {
		max_ := res[0]
		for _, v := range res[1:] {
			if v > max_ {
				max_ = v
			}
		}
		return max_
	}

	return 0
}
