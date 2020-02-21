# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == "(":
                stack.append(c)
                continue
            if c == ")" and stack:
                stack.pop()
                count += 2

        return count


def test_case(s: str, res: int):
    i = Solution()
    assert i.longestValidParentheses(s) == res
