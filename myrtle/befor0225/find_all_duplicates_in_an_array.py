# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 只需要 O(n) 关键在于 n 的取值
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            key = n - 1 if n >= 0 else -n - 1
            if nums[key] < 0:
                res.append(key + 1)
            else:
                nums[key] = -nums[key]

        return res


def test_case(nums: List[int]) -> List[int]:
    s = Solution()
    return s.findDuplicates(nums)
