# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0

        no_deletion_sum = arr[0]
        one_deletion_sum = 0
        from math import inf
        res = -inf

        for num in arr[1:]:
            one_deletion_sum = max(no_deletion_sum, one_deletion_sum + num)
            no_deletion_sum = max(no_deletion_sum + num, num)
            res = max(res, no_deletion_sum, one_deletion_sum)

        return max(res, no_deletion_sum)


