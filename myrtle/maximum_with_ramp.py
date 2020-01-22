# https://leetcode.com/problems/maximum-width-ramp/
from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        if not A:
            return 0

        if len(A) == 2:
            return 1 if A[1] >= A[0] else 0

        stack = []
        ramp = 0
        i = len(A) - 1

        while i >= 0:
            v = A[i]
            if not stack:
                stack.append(i)
                print(f'not stack append: {stack}')
                i -= 1
                continue

            if v > A[stack[-1]]:
                stack.append(i)
                print(f'stack append: {stack}')
                i -= 1
                continue

            k = len(stack) - 1
            while k >= 0:
                print(f'k index: {k}, cur value: {v}, stack value: {A[stack[k]]}')
                if v <= A[stack[k]]:
                    print(f'update ramp: {stack} {stack[k]} - {i}')
                    ramp = max(ramp, stack[k] - i)
                k -= 1
            i -= 1

        return ramp


def test_case(n: List[int]) -> int:
    s = Solution()
    return s.maxWidthRamp(n)





