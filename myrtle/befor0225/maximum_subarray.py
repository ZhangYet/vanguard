from typing import List


class Solution(object):
    def maxSubArray(self, nums: List) -> int:
        if not nums:
            return 0

        max_sum = cur_sum = nums[0]
        for num in nums[1:]:
            cur_sum += num
            if cur_sum < num:
                cur_sum = num
            if max_sum < cur_sum:
                max_sum = cur_sum

        return max_sum


# 没有理解透彻，需要复习
