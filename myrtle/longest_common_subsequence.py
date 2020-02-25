# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        row_nums = len(text1)
        col_nums = len(text2)

        dp = [[0] * col_nums for _ in range(row_nums)]

        flag = False
        for col in range(col_nums):
            if text2[col] == text1[0] or flag:
                dp[0][col] = 1
                flag = True

        flag = False
        for row in range(row_nums):
            if text2[0] == text1[row] or flag:
                dp[row][0] = 1
                flag = True

        for row in range(1, row_nums):
            for col in range(1, col_nums):
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
                if text2[col] == text1[row]:
                    dp[row][col] = max(dp[row][col], dp[row - 1][col - 1] + 1)

        return dp[row_nums - 1][col_nums - 1]


def test_case(text1: str, text2: str, res: int):
    s = Solution()
    assert s.longestCommonSubsequence(text1, text2) == res
