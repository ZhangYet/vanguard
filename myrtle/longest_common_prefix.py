# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        records = set()
        standard = strs[0]
        prefix = ""
        for i in range(len(standard) + 1):
            prefix = standard[:i]
            records.add(prefix)
            for s in strs[1:]:
                if len(s) < i:
                    return standard[: i - 1]
                if s[:i] not in records:
                    return standard[: i - 1]
        return prefix


def test_case(strs: List[str], res: str):
    s = Solution()
    assert s.longestCommonPrefix(strs) == res
