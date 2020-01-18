# https://leetcode.com/problems/next-greater-element-ii/
from typing import List

# 这样直接找会超时
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        if len(nums) == 1:
            return [-1]

        new_nums = nums + nums
        l = len(nums)
        res = [0] * l
        index = 0
        while index < l:
            cur = index + 1
            while cur < 2 * l and new_nums[cur] <= nums[index]:
                cur += 1
            if cur >= 2 * l:
                res[index] = -1
            else:
                res[index] = new_nums[cur]
            index += 1

        return res

def test_case(l: List[int]) -> List[int]:
    s = Solution()
    return s.nextGreaterElements(l)