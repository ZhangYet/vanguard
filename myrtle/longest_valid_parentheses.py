# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        index = ["0"] * len(s)
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
                i += 1
                continue
            if s[i] == ")" and stack:
                index[i] = "1"
                index[stack.pop()] = "1"
            i += 1

        count = max([len(s) for s in "".join(index).split("0")])
        return count


def test_case(s: str, res: int):
    i = Solution()
    assert i.longestValidParentheses(s) == res
