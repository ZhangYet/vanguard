# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List


def same_direction(nums: List[int], up: bool) -> bool:
    if len(nums) == 1:
        return True

    if up:
        return all([nums[i] < nums[i+1] for i in range(len(nums) - 1)])

    return all([nums[i] > nums[i+1] for i in range(len(nums) - 1)])


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) < 3:
            return -1

        peek = max(A)
        peek_index = A.index(peek)
        if A[peek_index+1] == peek:
            return -1
        if not same_direction(A[:peek_index], True):
            return -1
        if not same_direction(A[peek_index+1:], False):
            return -1
        return peek_index
