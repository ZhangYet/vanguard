# https://leetcode.com/problems/happy-number/
# 问题的关键是判断退出条件
# 我们可以把所有和存起来，一旦发现重复，就可以判断 False
class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(n: int) -> int:
            if n < 10:
                return n ** 2

            return (n % 10) ** 2 + digit_square_sum(n // 10)

        records = set()
        while n != 1:
            records.add(n)
            n = digit_square_sum(n)
            if n in records:
                return False
        return True
