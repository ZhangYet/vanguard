package goal

import (
	"testing"
)

func Test_mergeKLists(t *testing.T) {
	l1 := GenListNodeFromSlice([]int{1, 4, 5})
	l2 := GenListNodeFromSlice([]int{1, 3, 4})
	l3 := GenListNodeFromSlice([]int{2, 6})
	want := GenListNodeFromSlice([]int{1, 1, 2, 3, 4, 4, 5, 6})
	type args struct {
		lists []*ListNode
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		{
			name: "case1",
			args: args{
				lists: []*ListNode{l1, l2, l3},
			},
			want: want,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mergeKLists(tt.args.lists); !CompareList(got, tt.want) {
				t.Errorf("mergeKLists() = %v, want %v", got.ToSlice(), tt.want.ToSlice())
			}
		})
	}
}
