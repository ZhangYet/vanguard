# https://leetcode.com/problems/find-k-closest-elements/
# 这道题的麻烦在于，x 未必在 arr 中
# 先构造一个距离列，然后用堆
# 可行，但是比较慢
# 参考这种解法重新做一次： https://leetcode.com/problems/find-k-closest-elements/discuss/521857/python-solution
# 改天
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distance = [(abs(x - n), i) for i, n in enumerate(arr)]
        import heapq

        index = [d[1] for d in heapq.nsmallest(k, distance, key=lambda x: x[0])]
        index = sorted(index)
        return [arr[i] for i in index]


def test_case(arr: List[int], k: int, x: int) -> List[int]:
    s = Solution()
    return s.findClosestElements(arr, k, x)
