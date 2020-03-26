package goal

import (
	"strconv"
)

// https://leetcode.com/problems/additive-number/
// backtrack 但是我不熟

func additive(s string, index int, ans []string) bool {
	if index == len(s) && len(ans) > 2 {
		return true
	}
	res := false
	for i := index; i < len(s); i++ {
		p := s[index : i+1]
		if len(p) > 1 && p[0] == '0' {
			continue
		}
		if len(ans) >= 2 {
			one, _ := strconv.Atoi(ans[len(ans)-2])
			two, _ := strconv.Atoi(ans[len(ans)-1])
			pI, _ := strconv.Atoi(p)
			if one+two != pI {
				continue
			}
		}
		ans = append(ans, p)
		res = res || additive(s, i+1, ans)
		ans = ans[:len(ans)-1]
	}
	return res
}

func isAdditiveNumber(num string) bool {
	ans := make([]string, 0)
	return additive(num, 0, ans)
}
