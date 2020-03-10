# https://leetcode.com/problems/is-subsequence/
# 这就递归解决应该可以了
# 但是递归解法会超内存
# 但其实两个指针可以解决的
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t:
            return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])

        return self.isSubsequence(s, t[1:])


def test_case(s: str, t: str) -> bool:
    i = Solution()
    return i.isSubsequence(s, t)
        
