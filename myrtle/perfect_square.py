# Legendre's three-square theorem
# https://leetcode.com/problems/perfect-squares/submissions/
class Solution:
    def numSquares(self, n: int) -> int:
        from math import floor, sqrt

        root = floor(sqrt(n))
        if n - root ** 2 == 0:
            return 1

        for i in range(root, 0, -1):
            left_root = int(sqrt(n - i**2))
            if left_root ** 2 + i **2 == n:
                return 2

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        return 3


def test_case(n: int):
    s = Solution()
    return s.numSquares(n)