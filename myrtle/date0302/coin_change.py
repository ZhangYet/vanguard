# https://leetcode.com/problems/coin-change
# 尝试使用 BFS 去做
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount or not coins:
            return 0
        from collections import deque

        nodes = deque({(amount, 0)})
        visited = {amount}

        def neighbors(val: int):
            for coin in coins:
                yield val - coin

        while nodes:
            cur = nodes.popleft()
            if cur[0] == 0:
                return cur[1]

            if cur[0] < 0:
                continue

            for n in neighbors(cur[0]):
                if n not in visited:
                    nodes.append((n, cur[1] + 1))
                    visited.add(n)

        return -1


def test_case(coins: List[int], amount: int) -> int:
    s = Solution()
    return s.coinChange(coins, amount)
