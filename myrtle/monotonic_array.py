# https://leetcode.com/problems/monotonic-array/
from typing import List


class Solution2:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A or len(A) < 3:
            return True

        length = len(A)
        count = 0
        for i in range(length - 1):
            if count > 0:
                if A[i + 1] < A[i]:
                    return False
            elif count < 0:
                if A[i + 1] > A[i]:
                    return False
            else:
                count = A[i + 1] - A[i]

        return True


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A or len(A) < 3:
            return True

        UP = 1
        DOWN = -1
        EQUAL = 0
        CHAOS = -2

        def _monotonic(nums: List[int]) -> int:
            if len(nums) == 2:
                if nums[0] < nums[1]:
                    return UP
                if nums[0] > nums[1]:
                    return DOWN
                return EQUAL

            tail_status = _monotonic(nums[1:])
            if tail_status == CHAOS:
                return CHAOS

            if tail_status == EQUAL:
                return _monotonic(nums[:2])

            if tail_status == UP:
                return CHAOS if nums[0] > nums[1] else UP

            if tail_status == DOWN:
                return CHAOS if nums[0] < nums[1] else DOWN

        return _monotonic(A) != CHAOS


def test_case(nums: List[int]) -> bool:
    s = Solution2()
    return s.isMonotonic(nums)
