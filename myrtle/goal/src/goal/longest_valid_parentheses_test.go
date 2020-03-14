package goal

import "testing"

func Test_longestValidParentheses(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "case1",
			args: args{"(()"},
			want: 2,
		},
		{
			name: "case2",
			args: args{")()())"},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestValidParentheses(tt.args.s); got != tt.want {
				t.Errorf("LongestValidParentheses() = %v, want %v", got, tt.want)
			}
		})
	}
}
