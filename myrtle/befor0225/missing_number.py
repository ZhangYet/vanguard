# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        from math import inf

        l = len(nums)
        nums.append(inf)

        for num in nums[:l]:
            nums[num] = -nums[num] if nums[num] > 0 else -inf

        for i in range(l + 1):
            if nums[i] >= 0:
                return i


def test_case(nums: List[int]):
    s = Solution()
    return s.missingNumber(nums)
