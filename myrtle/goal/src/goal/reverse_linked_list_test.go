package goal

import (
	"reflect"
	"testing"
)

func Test_travelReverseList(t *testing.T) {
	head1 := makeListNode([]int{1, 2, 3, 4})
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "trivalCase",
			args: args{
				head: makeListNode([]int{1, 2, 3, 4}),
			},
			want: []int{1, 2, 3, 4},
		},
		{
			name: "ReverseCase",
			args: args{
				head: reverseList(head1),
			},
			want: []int{4, 3, 2, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := travelReverseList(tt.args.head); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("travelReverseList() = %v, want %v", got, tt.want)
			}
		})
	}
}
