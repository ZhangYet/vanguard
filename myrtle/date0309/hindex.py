# https://leetcode.com/problems/h-index/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        i, paper_n = 1, len(citations)
        while i <= paper_n:
            n = paper_n - i + 1
            if citations[i-1] >= n:
                return n
            i += 1
        return 0
