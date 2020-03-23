package goal

func isPalindrome(head *ListNode) bool {
	data := []int{}
	for {
		if head == nil {
			break
		}
		data = append(data, head.Val)
		if head.Next == nil {
			break
		}
		head = head.Next
	}
	if len(data) <= 1 {
		return true
	}
	h, t := 0, len(data)-1
	for {
		if h >= t {
			return true
		}
		if data[h] != data[t] {
			return false
		}
		h += 1
		t -= 1
	}
}
