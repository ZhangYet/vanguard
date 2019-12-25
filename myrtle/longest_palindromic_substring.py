class Solution:
    def longestPalindrome(self, s: str) -> str:

        def _longest_palindrome(s: str):
            print(f'enter: {s}')
            input_len = len(s)
            if input_len <= 1:
                return s

            if s[0] == s[-1]:
                sub_palindrome = _longest_palindrome(s[1:-1])
                if len(sub_palindrome) == input_len - 2:
                    print(f'situation one')
                    return s

            left_sub_palindrome = _longest_palindrome(s[:-1])
            # right_sub_palindrome = _longest_palindrome(s[1:])
            print('left or right')
            return left_sub_palindrome #if len(left_sub_palindrome) >= len(right_sub_palindrome) else right_sub_palindrome

        return _longest_palindrome(s)


def test_solution(s: str):
    sol = Solution()
    return sol.longestPalindrome(s)