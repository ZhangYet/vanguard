# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res: List[List[int]] = [nums, []]
        def _rev(nums: List[int]):
            if len(nums) == 1:
                if nums not in res:
                    res.append(nums)
                    return

            for i in range(len(nums)):
                others = nums[:i] + nums[(i+1):]
                if others not in res:
                    res.append(others)
                    _rev(others)
                if [nums[i]] not in res:
                    res.append([nums[i]])

        _rev(nums)
        return res


def test_case(nums: List[int]) -> List[List[int]]:
    s = Solution()
    return s.subsets(nums)