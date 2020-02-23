from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        N = len(A)

        def ave(i, j):
            return (P[j] - P[i]) / (j - i)

        dp = [ave(i, N) for i in range(N)]
        for k in range(K - 1):
            for i in range(N - 1):
                dp[i] = max([ave(i, j) + dp[j] for j in range(i + 1, N)])

        return dp[0]
