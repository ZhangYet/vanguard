# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 1, len(numbers)
        while low < high:
            s = numbers[low - 1] + numbers[high - 1]
            if s == target:
                return [low, high]

            if s < target:
                low += 1

            if s > target:
                high -= 1

        return [-1, -1]
