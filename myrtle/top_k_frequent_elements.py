# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict

        record = defaultdict(int)
        for num in nums:
            record[num] += 1
        r = [(v, k) for k, v in record.items()]
        t = heapq.nlargest(k, r, key=lambda x: x[0])
        return [x[1] for x in t]


def test_case():
    t = [1, 1, 1, 2, 2, 3]
    s = Solution()
    return s.topKFrequent(t, 2)
