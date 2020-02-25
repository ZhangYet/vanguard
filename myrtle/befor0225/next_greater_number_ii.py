# https://leetcode.com/problems/next-greater-element-ii/
from typing import List

# 这样直接找会超时
# 别以为耍这种小把戏就可以过关！
# 用 stack!
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        l = len(nums)
        L = 2 * l
        res = [-1] * l
        stack = []

        cur = L - 1
        while cur >= 0:
            next_greater_num = -1 if not stack else nums[stack[-1]]
            index = cur if cur < l else cur - l


            if not stack:
                stack.append(index)
                cur -= 1
                continue

            if nums[stack[-1]] > nums[index]:
                res[index] = nums[stack[-1]]
                stack.append(index)
                cur -= 1
                continue

            while stack:
                if nums[stack[-1]] <= nums[index]:
                    stack.pop()
                else:
                    res[index] = nums[stack[-1]]
                    break

            stack.append(index)
            cur -= 1

        return res

def test_case(l: List[int]):
    s = Solution()
    return s.nextGreaterElements(l)