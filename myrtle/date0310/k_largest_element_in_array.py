# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List

# 直接用标准库的 heapq 做吧


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heapq.heapify(nums)
        res = heapq.nlargest(k, nums)
        print(res)
        return res[-1]
