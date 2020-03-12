# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, max_len, n = '', 0, len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            res = s[i]
            max_len = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                d[i][i+1] = 1
                res = s[i:i+1]
                max_len = 2

        for i in range(n):
            for j in range(i-1):
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = 1
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        res = s[j: i+1]
        return res

# 抽空把这个 DP 的递推关系写出来吧
