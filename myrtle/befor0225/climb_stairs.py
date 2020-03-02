# https://leetcode.com/problems/climbing-stairs/submissions/
# 因为其实就是 Fibonacci 数列，所以直接用公式偷懒了
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
