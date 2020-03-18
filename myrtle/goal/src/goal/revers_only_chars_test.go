package goal

import "testing"

func Test_reverseOnlyLetters(t *testing.T) {
	type args struct {
		S string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "case1",
			args: args{
				S: "a-bC-dEf-ghIj",
			},
			want: "j-Ih-gfE-dCba",
		},
		{
			name: "case2",
			args: args{
				S: "ab-cd",
			},
			want: "dc-ba",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reverseOnlyLetters(tt.args.S); got != tt.want {
				t.Errorf("reverseOnlyLetters() = %v, want %v", got, tt.want)
			}
		})
	}
}
