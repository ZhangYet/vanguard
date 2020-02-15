# https://leetcode.com/problems/total-hamming-distance/
from typing import List


def fast_hamming_weight(num: int):
    s = 0
    while num:
        s += 1
        num &= num - 1

    return s


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += sum([fast_hamming_weight(nums[i] ^ x) for x in nums[i:]])

        return s


def test_case(nums: List[int]) -> int:
    s = Solution()
    return s.totalHammingDistance(nums)
