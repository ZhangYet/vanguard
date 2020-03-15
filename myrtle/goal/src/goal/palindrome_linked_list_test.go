package goal

import (
	"testing"
)

func makeListNode(nums []int) *ListNode {
	head := &ListNode{Val: nums[0]}
	cur := head
	for _, num := range nums[1:] {
		tmp := &ListNode{Val: num}
		cur.Next = tmp
		cur = cur.Next
	}
	return head
}

func Test_isPalindrome(t *testing.T) {
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "case1",
			args: args{
				head: makeListNode([]int{1, 2, 2, 1}),
			},
			want: true,
		},
		{
			name: "case2",
			args: args{
				head: makeListNode([]int{1, 2}),
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.head); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
