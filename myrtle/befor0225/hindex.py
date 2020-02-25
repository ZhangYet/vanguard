# https://leetcode.com/problems/h-index/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        while citations and citations[-1] < len(citations):
            citations.pop()

        return len(citations)


def test_case(c: List[int]) -> int:
    s = Solution()
    return s.hIndex(c)
