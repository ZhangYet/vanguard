# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
from typing import List
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        import heapq
        data = []

        head_1, head_2 = 0, 0
        len_1, len_2 = len(nums1), len(nums2)
        for _ in range(k):
            if head_1 >= len_1 or head_2 >= len_2:
                break
            if nums1[head_1] < nums2[head_2]:
                for y in nums2[head_2:]:
                    heapq.heappush(data, [nums1[head_1], y])
                head_1 += 1
            else:
                for x in nums1[head_1:]:
                    heapq.heappush(data, [x, nums2[head_2]])
                head_2 += 1
        return heapq.nsmallest(k, data, key=sum)
                
