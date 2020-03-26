package goal

func hIndex(citations []int) int {
	for i := len(citations) - 1; i >= 0; i++ {
		if citations[i] >= i+1 {
			return i + 1
		}
	}
	return 0
}
