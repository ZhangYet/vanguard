package goal

func isMonotonic(A []int) bool {
	l := len(A)
	if l <= 2 {
		return true
	}
	count := 0
	for i := 0; i < l-1; i++ {
		if count > 0 {
			if A[i] < A[i+1] {
				return false
			}
		} else if count < 0 {
			if A[i] > A[i+1] {
				return false
			}
		} else {
			count = A[i] - A[i+1]
		}
	}
	return true
}

// 最大的问题是连续等于的情况会干扰我们，所以我们其实用 count 记录上一次有差异的情况
// 如果 count 不等于0， 那么它不会被更新，如果它等于0，那么它不影响结果
