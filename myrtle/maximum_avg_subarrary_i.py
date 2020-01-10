# https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0

        i = 0
        L = len(nums)
        cur_sum = sum(nums[i:(i+k)])
        maximum = cur_sum
        while (i+k) < L:
            cur_sum -= nums[i]
            cur_sum += nums[i+k]
            if cur_sum > maximum:
                maximum = cur_sum
            i += 1
        return maximum / k