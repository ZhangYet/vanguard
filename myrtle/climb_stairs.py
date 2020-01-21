# https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1
        from math import sqrt
        c = sqrt(5)
        left = (1 + c) / 2
        right = (1 - c) / 2
        res = 1 / c * (left ** n + right ** n)
        return round(res)


def test_case(n: int) -> int:
    s = Solution()
    return s.climbStairs(n)