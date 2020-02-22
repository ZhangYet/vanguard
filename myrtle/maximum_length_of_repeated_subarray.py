# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
from typing import List
from utils import print_matrix


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0

        dp = [[0] * len(A) for _ in B]
        row_nums = len(B)
        col_nums = len(A)

        def _lambda(col: int, row: int, l: int) -> bool:
            return A[col - l : col] == B[row - l : row]

        for row in range(row_nums):
            for col in range(col_nums):
                if row == 0 and col == 0:
                    dp[0][0] = 1 if A[0] == B[0] else 0
                    continue
                if row == 0:
                    dp[0][col] = 1 if A[col] == B[0] else dp[0][col - 1]
                    continue

                if col == 0:
                    dp[row][0] = 1 if A[0] == B[row] else dp[row - 1][0]
                    continue

                if A[col] == B[row] and _lambda(col, row, dp[row - 1][col - 1]):
                    dp[row][col] = max(
                        dp[row - 1][col], dp[row][col - 1], 1 + dp[row - 1][col - 1]
                    )
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        print_matrix(dp)
        return dp[row_nums - 1][col_nums - 1]


def test_case(A: List[int], B: List[int], res: int):
    s = Solution()
    assert s.findLength(A, B) == res
