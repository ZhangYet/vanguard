package goal

// 关键是用栈

type dupStack []int

func (this *dupStack) Pop() int {
	l := len(*this)
	res := (*this)[l-1]
	*this = (*this)[:l-1]
	return res
}

func (this *dupStack) Empty() bool {
	return len(*this) <= 0
}

func removeDuplicates(S string) string {
	l := len(S)
	if l <= 1 {
		return S
	}

	prev, cur := 0, 1
	removeIndex := make(map[int]bool)
	stack := make(dupStack, 0)
	for {
		if cur >= l {
			break
		}
		if S[prev] != S[cur] {
			stack = append(stack, prev)
			prev = cur
			cur = prev + 1
			continue
		}
		if S[prev] == S[cur] {
			removeIndex[prev] = true
			removeIndex[cur] = true
			cur += 1
			if cur >= l {
				break
			}
			if stack.Empty() {
				prev = cur
				cur = prev + 1
				continue
			}
			prev = stack.Pop()
		}
	}
	res := []rune{}
	for idx, c := range S {
		if _, ok := removeIndex[idx]; ok {
			continue
		}
		res = append(res, c)
	}
	return string(res)
}
