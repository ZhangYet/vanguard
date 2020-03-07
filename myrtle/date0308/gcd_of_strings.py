# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# 这道题还是有点意思的，参考辗转相除的方法，如果有一个 str 变成空字符串，检查非空的那个是否公共字串
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def _div(d1: str, d2: str) -> str:
            if len(d2) > len(d1):
                d1, d2 = d2, d1

            if not d2:
                return d1

            return _div(d2, d1[len(d2) :])

        r = _div(str1, str2)
        return r if (r in str1 and r in str2) else ""


def test_case(str1: str, str2: str) -> str:
    s = Solution()
    return s.gcdOfStrings(str1, str2)
