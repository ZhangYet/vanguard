package goal

import "unicode"

func reverseOnlyLetters(S string) string {
	records := make([]rune, len(S))

	low, high := 0, len(S)-1
	for {
		if low >= high {
			if low == high {
				records[low] = rune(S[low])
			}
			break
		}
		if !unicode.IsLetter(rune(S[low])) {
			records[low] = rune(S[low])
			low += 1
			continue
		}
		if !unicode.IsLetter(rune(S[high])) {
			records[high] = rune(S[high])
			high -= 1
			continue
		}
		records[low], records[high] = rune(S[high]), rune(S[low])
		low += 1
		high -= 1
	}
	return string(records)
}
