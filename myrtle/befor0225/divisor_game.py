# https://leetcode.com/problems/divisor-game/
# 最快的方法是：
# class Solution:
#     def divisorGame(self, N: int) -> bool:
#         return not (N & 1)
# 诀窍在于：1 是任意整数的因素
from typing import List


class Solution:
    def get_factors(self, N: int) -> List[int]:
        import math

        res = [1]
        for i in range(2, round(math.sqrt(N))):
            if N % i == 0:
                res.append(i)
        return res

    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        if N == 2:
            return True
        if N == 3:
            return False

        game_result = [False] * (N + 1)
        game_result[1] = False
        game_result[2] = True
        game_result[3] = False

        for i in range(4, N + 1):
            factors = self.get_factors(i)
            for factor in factors:
                if (factor % 2 == 1) and not game_result[i - factor]:
                    game_result[i] = True
                    break
                if (factor % 2 == 0) and game_result[i - factor]:
                    game_result[i] = True
                    break
        return game_result[N]


def test_case(i: int, ex: bool):
    s = Solution()
    assert s.divisorGame(i) == ex
