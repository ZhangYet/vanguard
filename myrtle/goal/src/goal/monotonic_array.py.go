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
