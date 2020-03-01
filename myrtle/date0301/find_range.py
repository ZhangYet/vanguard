# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 边边角角的情况挺难搞的
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # bin_search
        low, high = 0, len(nums) - 1
        middle = low + (high - low) // 2
        while low <= high:
            if nums[middle] == target:
                low = middle
                break
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
            middle = low + (high - low) // 2

        try:
            if nums[low] != target:
                return [-1, -1]
        except IndexError:
            return [-1, -1]

        left, right, right_bound = low, low, len(nums)
        while (left > -1 and nums[left] == target) or (
            right < right_bound and nums[right] == target
        ):
            if left > -1 and nums[left] == target:
                left -= 1
            if right < right_bound and nums[right] == target:
                right += 1

            if left == -1 and right == right_bound:
                break

        return [left + 1, right - 1]


def test_case(nums: List[int], t: int) -> List[int]:
    s = Solution()
    return s.searchRange(nums, t)
