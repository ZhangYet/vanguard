# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t:
            return False

        dp = [[0] * len(s) for _ in t]

        flag = False
        for i in range(len(s)):
            if s[i] == t[0] or flag:
                dp[0][i] = 1
                flag = True

        flag = False
        for i in range(len(t)):
            if t[i] == s[0] or flag:
                dp[i][0] = 1
                flag = True

        for col in range(1, len(s)):
            for row in range(1, len(t)):
                if s[col] == t[row]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return len(s) == dp[len(t) - 1][len(s) - 1]


def test_case(s: str, t: str, res: bool):
    i = Solution()
    assert i.isSubsequence(s, t) == res
