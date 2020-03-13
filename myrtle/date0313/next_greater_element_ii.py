# https://leetcode.com/problems/next-greater-element-ii/
# 考虑使用 next greater node in list 的方法做

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        from collections import deque
        stack = deque()
        len_nums = len(nums)
        res = [-1] * len_nums
        elems = nums + nums

        for i in range(len(elems)):
            while stack and elems[stack[-1]] < elems[i]:
                res[stack[-1] % len_nums] = elems[i]
                stack.pop()
            stack.append(i)
        return res
