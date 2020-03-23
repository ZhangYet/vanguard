package goal

import (
	"testing"
)

func Test_partition(t *testing.T) {
	type args struct {
		head *ListNode
		x    int
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		{
			name: "case1",
			args: args{
				head: GenListNodeFromSlice([]int{1, 4, 3, 2, 5, 2}),
				x:    3,
			},
			want: GenListNodeFromSlice([]int{1, 2, 2, 4, 3, 5}),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partition(tt.args.head, tt.args.x); !CompareList(tt.want, got) {
				t.Errorf("partition() = %v, want %v", got.ToSlice(), tt.want.ToSlice())
			}
		})
	}
}
