package goal

import (
	"reflect"
	"testing"
)

func makeFreqSubtreeSumCase() (*TreeNode, *TreeNode) {
	t1 := TreeNode{Val: 5}
	t2 := TreeNode{Val: 2}
	t3 := TreeNode{Val: -3}
	t1.Left = &t2
	t1.Right = &t3
	return &t1, nil
}

func Test_findFrequentTreeSum(t *testing.T) {
	t1, _ := makeFreqSubtreeSumCase()
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "case1",
			args: args{
				root: t1,
			},
			want: []int{2, -3, 4},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findFrequentTreeSum(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findFrequentTreeSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
