package goal

import "testing"

func Test_longestOnes(t *testing.T) {
	type args struct {
		A []int
		K int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "example1",
			args: args{
				A: []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
				K: 2,
			},
			want: 6,
		},
		{
			name: "example2",
			args: args{
				A: []int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1},
				K: 3,
			},
			want: 10,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestOnes(tt.args.A, tt.args.K); got != tt.want {
				t.Errorf("longestOnes() = %v, want %v", got, tt.want)
			}
		})
	}
}
