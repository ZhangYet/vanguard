# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = ""
        record = set()
        for i in range(len(strs[0])+1):
            prefix = strs[0][:i]
            record.add(prefix)
            for s in strs[1:]:
                if len(s) < i or s[:i] not in record:
                    return strs[0][:i-1]

        return prefix
