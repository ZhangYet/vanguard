# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 看起来很简单啊
from typing import List


class Solution:
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return [c for c in self.mapping[digits]]

        return [
            c + x
            for x in self.letterCombinations(digits[1:])
            for c in self.mapping[digits[0]]
        ]


def test_case(digits: str):
    s = Solution()
    return s.letterCombinations(digits)
