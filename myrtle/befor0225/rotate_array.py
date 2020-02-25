# https://leetcode.com/problems/rotate-array/solution/
from typing import List


def reverse(nums: List[int], start, end) -> None:
    if not nums:
        return

    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
