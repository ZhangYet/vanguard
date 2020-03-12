# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left, n = 0, 0, len(s)
        seen = set()
        for right in range(n):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[left] != s[right]:
                    seen.discard(s[left])
                    left += 1
                left += 1
            res = max(res, right - left + 1)
        return res
