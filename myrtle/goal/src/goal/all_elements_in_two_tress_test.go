package goal

import (
	"reflect"
	"testing"
)

func newSetupCase() (*TreeNode, *TreeNode) {
	l1 := TreeNode{Val: 2}
	l2 := TreeNode{Val: 1}
	l3 := TreeNode{Val: 4}
	l1.Left, l1.Right = &l2, &l3
	r1 := TreeNode{Val: 1}
	r2 := TreeNode{Val: 0}
	r3 := TreeNode{Val: 3}
	r1.Left, r1.Right = &r2, &r3
	return &l1, &r1

}

func Test_getAllElements(t *testing.T) {
	root1, root2 := newSetupCase()
	type args struct {
		root1 *TreeNode
		root2 *TreeNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "case1",
			args: args{
				root1: root1,
				root2: root2,
			},
			want: []int{0, 1, 1, 2, 3, 4},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getAllElements(tt.args.root1, tt.args.root2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getAllElements() = %v, want %v", got, tt.want)
			}
		})
	}
}
