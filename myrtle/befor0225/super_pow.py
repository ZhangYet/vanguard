# https://leetcode.com/problems/super-pow/
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return (a % 1337) ** (int("".join(map(str, b))) % 570) % 1337


def test_case(a: int, b: List[int]) -> int:
    s = Solution()
    return s.superPow(a, b)
