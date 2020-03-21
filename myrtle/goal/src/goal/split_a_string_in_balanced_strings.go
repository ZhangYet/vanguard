package goal

// https://leetcode.com/problems/split-a-string-in-balanced-strings/
func balancedStringSplit(s string) int {
	z, count := 0, 0
	for _, c := range s {
		if c == 'L' {
			z += 1
		} else {
			z -= 1
		}
		if z == 0 {
			count += 1
		}
	}
	return count
}
