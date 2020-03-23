package goal

import (
	"fmt"
	"strings"
)

// https://leetcode.com/problems/length-of-last-word/
func lengthOfLastWord(s string) int {
	wordList := strings.Split(strings.Trim(s, " "), " ")
	l := len(wordList)
	fmt.Printf("wordList: %v, len: %d\n", wordList, l)
	if l <= 0 {
		return 0
	}
	return len(wordList[l-1])
}
