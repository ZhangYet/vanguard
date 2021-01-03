package goal

// https://leetcode.com/problems/max-consecutive-ones-iii/

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func longestOnes(A []int, K int) int {
	ret := 0
	left, right := 0, 0
	L := len(A)
	for left < L {
		if right < L && ((A[right] == 0 && K > 0) || A[right] == 1) {
			right += 1
			if A[right] == 0 {
				K -= 1
			}
		} else {
			if K == 0 || (right == L && K > 0) {
				ret = max(ret, right-left)
			}
			if A[left] == 0 {
				K += 1
			}
			L += 1
		}
	}
	return ret
}
