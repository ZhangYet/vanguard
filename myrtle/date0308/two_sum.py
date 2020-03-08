# https://leetcode.com/problems/two-sum/
# 结果更慢了
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, v in enumerate(nums):
            if target - v in pos:
                return [pos[target - v], i]
            pos[v] = i

        return []
