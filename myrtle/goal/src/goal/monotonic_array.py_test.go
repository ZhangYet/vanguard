package goal

import "testing"

func Test_isMonotonic(t *testing.T) {
	type args struct {
		A []int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "case1",
			args: args{
				A: []int{1, 2, 4, 5},
			},
			want: true,
		},
		{
			name: "case2",
			args: args{
				A: []int{2, 2, 2},
			},
			want: true,
		},
		{
			name: "case3",
			args: args{
				A: []int{1, 3, 2},
			},
			want: false,
		},
		{
			name: "case4",
			args: args{
				A: []int{2, 1, 1, 1, 1},
			},
			want: true,
		},
		{
			name: "case5",
			args: args{
				A: []int{2, 1, 1, 1, 2},
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isMonotonic(tt.args.A); got != tt.want {
				t.Errorf("isMonotonic() = %v, want %v", got, tt.want)
			}
		})
	}
}
