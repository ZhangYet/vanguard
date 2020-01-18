# https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        def _add_digit(num: int):
            if num < 10:
                return num

            return _add_digit(_add_digit(num // 10) + num % 10)

        return _add_digit(num)


def test_case(i: int) -> int:
    s = Solution()
    return s.addDigits(i)
