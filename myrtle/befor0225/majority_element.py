# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict

        record = defaultdict(int)
        L = len(nums)
        t = L // 2
        for num in nums:
            record[num] += 1
            if record[num] > t:
                return num

        return 0