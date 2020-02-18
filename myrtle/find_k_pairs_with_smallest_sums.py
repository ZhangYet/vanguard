# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        data = []
        import heapq

        i, j = 0, 0
        for _ in range(k):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    for y in nums2[j:]:
                        heapq.heappush(data, [nums1[i], y])
                    i += 1
                else:
                    for x in nums1[i:]:
                        heapq.heappush(data, [x, nums2[j]])
                    j += 1

        return heapq.nsmallest(k, data, sum)


def test_case(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    s = Solution()
    return s.kSmallestPairs(nums1, nums2, k)


def case1():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    s = test_case(nums1, nums2, 3)
    return s
