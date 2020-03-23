package goal

import (
	"testing"
)

func Test_mergeTwoLists(t *testing.T) {
	l1 := GenListNodeFromSlice([]int{1, 2, 4})
	l2 := GenListNodeFromSlice([]int{1, 3, 4})
	res := GenListNodeFromSlice([]int{1, 1, 2, 3, 4, 4})
	type args struct {
		l1 *ListNode
		l2 *ListNode
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		{
			name: "case1",
			args: args{
				l1: l1,
				l2: l2,
			},
			want: res,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mergeTwoLists(tt.args.l1, tt.args.l2); !CompareList(got, tt.want) {
				t.Errorf("mergeTwoLists() = %v, want %v", got.ToSlice(), tt.want.ToSlice())
			}
		})
	}
}
