# https://leetcode.com/problems/base-7/
from typing import List

class Solution:
    def convertToBase7(self, num: int) -> str:

        def convert(num: int) -> List[int]:
            if num < 7:
                return [num]

            h: List[int] = convert(num // 7)
            h.append(num % 7)
            return h

        flag = '' if num > 0 else '-'
        n = num if num > 0 else -num
        return flag + ''.join([str(x) for x in convert(n)])