# https://leetcode.com/problems/isomorphic-strings/
# 这个没有想象中那么简单，它不是一个恺撒密码变换
# 只能靠记录了
# 简单的记录还不行，其实就是要双射嘛
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        record = {}
        for i in range(len(s)):
            k = s[i]
            if k in record and record[k] != t[i]:
                return False
            record[k] = t[i]

        return len(set(record.keys())) == len(set(record.values()))


def test_case():
    s = Solution()
    assert s.isIsomorphic("add", "egg") == True
    assert s.isIsomorphic("ab", "aa") == False
    assert s.isIsomorphic("ab", "ca") == True
