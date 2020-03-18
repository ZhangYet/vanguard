package goal

func count(start, L int) int {
	subArrayLen := L - start
	left := 0
	for i := 1; i < subArrayLen; i++ {
		left += i * i
	}
	right := (subArrayLen + 1) * subArrayLen / 2
	return left + right
}

func sumSubarrayMins(A []int) int {
	//fmt.Printf("A: %v\n", A)
	lenA := len(A)
	if lenA == 0 {
		return 0
	}

	if lenA == 1 {
		return A[0]
	}
	if lenA == 2 {
		if A[0] < A[1] {
			return A[0]*2 + A[1]
		} else {
			return A[1]*2 + A[0]
		}
	}
	mnIdx := 0
	mn := A[0]
	for i := 1; i < lenA; i++ {
		if A[i] < mn {
			mn = A[i]
			mnIdx = i
		}
	}
	left := sumSubarrayMins(A[:mnIdx])
	right := sumSubarrayMins(A[mnIdx+1:])
	n := lenA + (mnIdx * (lenA - mnIdx - 1)) // 原则上就差这一步了，就是计算有多少 sub array 包含了 mn
	sumMin := mn * n
	//fmt.Printf("left: %d, right: %d, sumMin: %d, n: %d\n", left, right, sumMin, n)

	return (left + right + sumMin) % 1000000007
}
