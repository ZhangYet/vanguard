# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s: str) -> int:

        def cal(s: str, level: int):
            if len(s) == 1:
                return (ord(s) - 64) * (26 ** (level - 1))

            return (ord(s[-1]) - 64) * (26 ** (level - 1)) + cal(s[:-1], level+1)

        return cal(s, 1)

def test_case(s: str) -> int:
    i = Solution()
    return i.titleToNumber(s)