package goal

import "math"

// https://leetcode.com/problems/nth-digit/
// 思路：先确定是几位数
// 思路没问题，处理好边界条件就好，不过当前的答案是搓的。

func calDigitAndRemain(n int) (int, int) {
	res := 1
	for {
		digits := 9 * res * int(math.Pow10(res-1))
		if n < digits {
			return n, res
		}
		n -= digits
		res += 1
	}
}

func getDigit(num, digit, r int) int {
	if r == 0 {
		r = digit
	}
	res := 0
	for i := digit - r; i >= 0; i-- {
		res = num % 10
		num /= 10
	}
	return res
}

func findNthDigit(n int) int {
	remain, digits := calDigitAndRemain(n)
	q, r := remain/digits, remain%digits
	num := q
	if r != 0 {
		num += 1
	}
	base := int(math.Pow10(digits))
	actualNum := base + num - 1
	return getDigit(actualNum, digits, r)
}
