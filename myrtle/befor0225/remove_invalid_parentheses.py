# https://leetcode.com/problems/remove-invalid-parentheses/
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def _is_valid(s: str):
            stack = []
            for c in s:
                if c == '(':
                    stack.append(c)

                if c == ')':
                    try:
                        stack.pop()
                    except IndexError:
                        return False

            return not stack

        res = []
        for i in range(len(s)):
            sub = s[:i] + s[(i+1):]
            if _is_valid(sub):
                res.append(sub)

        if _is_valid(s):
            res.append(s)

        if not res:
            return [""]

        return list(set(res))


def test_case(s: str):
    i = Solution()
    return i.removeInvalidParentheses(s)


