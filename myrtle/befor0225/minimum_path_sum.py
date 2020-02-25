# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row_num = len(grid)
        col_num = len(grid[0])

        dp = [[0] * col_num for _ in grid]

        for row in range(row_num):
            for col in range(col_num):
                if row == 0 and col == 0:
                    dp[row][col] = grid[0][0]
                    continue
                if row == 0:
                    dp[row][col] = grid[0][col] + dp[0][col - 1]
                    continue
                if col == 0:
                    dp[row][col] = grid[row][0] + dp[row - 1][0]
                    continue

                dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

        return dp[row_num - 1][col_num - 1]


def test_case(grid: List[List[int]], res: int):
    s = Solution()
    assert s.minPathSum(grid) == res
