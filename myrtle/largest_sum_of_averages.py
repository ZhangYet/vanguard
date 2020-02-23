# https://leetcode.com/problems/largest-sum-of-averages/
from typing import List
from utils import print_matrix


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = [[0] * len(A) for _ in range(K)]

        for group_num in range(K):
            for num_index in range(len(A)):
                if group_num == 0:
                    dp[group_num][num_index] = sum(A[: num_index + 1]) / (num_index + 1)
                    continue
                if group_num > num_index:
                    dp[group_num][num_index] = 0.0
                    continue

                dp[group_num][num_index] = max(
                    [
                        sum(A[i : num_index + 1]) / (num_index - i + 1)
                        + dp[group_num - 1][i]
                        for i in range(0, num_index)
                    ]
                )
        print_matrix(dp)
        return dp[K - 1][len(A) - 1]


def test_case():
    s = Solution()
    assert s.largestSumOfAverages([9, 1, 2, 3, 9], 3) == 20
