# https://leetcode.com/problems/longest-harmonious-subsequence/
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter

        counter = Counter(nums)
        res = 0
        for k, v in counter.items():
            high, low = k + 1, k - 1
            high_c, low_c = counter.get(high, 0), counter.get(low, 0)
            if high_c:
                high_c = v + high_c
            if low_c:
                low_c = v + low_c
            res = max(res, high_c, low_c)
        return res


def test_case(nums: List[int]) -> int:
    s = Solution()
    return s.findLHS(nums)
