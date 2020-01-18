# https://leetcode.com/problems/next-greater-element-ii/
from typing import List

# 这样直接找会超时
# 别以为耍这种小把戏就可以过关！
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        l = len(nums)
        res = [0] * l
        for i in range(l):
            new_nums = nums[(i+1):] + nums[:i]
            r = [x for x in new_nums if x > nums[i]]
            if not r:
                res[i] = -1
            else:
                res[i] = r[0]

        return res

def test_case(l: List[int]) -> List[int]:
    s = Solution()
    return s.nextGreaterElements(l)