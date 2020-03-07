# https://leetcode.com/problems/factorial-trailing-zeroes/
# 《编程之美》2.2
# 其实就是数5的个数
# 但是也不是那么简单啊
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n // 5
            n //= 5
        return res


def test_case(n: int) -> int:
    s = Solution()
    return s.trailingZeroes(n)
