# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t:
            return False

        ptr_s, ptr_t = 0, 0
        css = ""
        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                css += s[ptr_s]
                ptr_s += 1
                ptr_t += 1
            else:
                ptr_t += 1

        return css == s


def test_case(s: str, t: str, res: bool):
    i = Solution()
    assert i.isSubsequence(s, t) == res
