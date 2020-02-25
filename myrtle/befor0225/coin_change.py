# https://leetcode.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def _change(coins: List[int], amount: int) -> int:
            if amount in coins:
                return 1

            left = [amount - x for x in coins]
            if all([l < 0 for l in left]):
                return -1

            left_change = [_change(coins, x) for x in left if x > 0]
            left_change = [x for x in left_change if x > 0]
            if not left_change:
                return -1
            return 1 + min(left_change)

        res = _change(coins, amount)
        return 0 if res < 0 else res


def test_case(coins: List[int], amount: int) -> int:
    s = Solution()
    return s.coinChange(coins, amount)
