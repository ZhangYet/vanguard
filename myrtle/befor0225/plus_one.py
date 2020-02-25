# https://leetcode.com/problems/plus-one/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def _plus_one(digits: List[int]) -> List[int]:
            if not digits:
                return [1]
            tail = digits[-1] + 1
            if tail < 10:
                digits[-1] = tail
                return digits

            digits[-1] = 0
            head = _plus_one(digits[:-1])
            head.append(0)
            return head

        return _plus_one(digits)

def test_case(l: List[int]) -> List[int]:
    s = Solution()
    return s.plusOne(l)