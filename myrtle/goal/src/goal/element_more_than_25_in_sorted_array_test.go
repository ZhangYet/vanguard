package goal

import "testing"

func Test_findSpecialInteger(t *testing.T) {
	type args struct {
		arr []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "case1",
			args: args{
				arr: []int{1, 2, 2, 6, 6, 6, 6, 7, 10},
			},
			want: 6,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findSpecialInteger(tt.args.arr); got != tt.want {
				t.Errorf("findSpecialInteger() = %v, want %v", got, tt.want)
			}
		})
	}
}
