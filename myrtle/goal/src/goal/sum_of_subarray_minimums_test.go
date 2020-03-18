package goal

import "testing"

func Test_sumSubarrayMinsb(t *testing.T) {
	type args struct {
		A []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "case1",
			args: args{
				A: []int{3, 1, 2, 4},
			},
			want: 17,
		},
		{
			name: "case2",
			args: args{
				A: []int{62, 92, 97},
			},
			want: 467,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sumSubarrayMins(tt.args.A); got != tt.want {
				t.Errorf("sumSubarrayMins() = %v, want %v", got, tt.want)
			}
		})
	}
}
