# https://leetcode.com/problems/contiguous-array/
# 看起来还挺麻烦的，想不到 DP 解法
# 如果我们创建一个累积有多少1的数组，会不会有帮助？
# 主要是怎样判断我们找到最大了？
# 怎样处理那些前面有太多0的情况？
# 试试用类似 DP 的算法吧
# 看了这个答案： https://leetcode.com/problems/contiguous-array/discuss/485448/Python-3-Presum-%2B-hashtable-O(n)-clean-code-beats-93
# 真是妙啊，每一位如果是1就加1，如果是0就加-1，记录每种和初次出现的 index，下次再遇到同样的和
# 把当前的 index 减去第一次出现这种和的 index，中间就是0，1相等的子数组
# 注意出现0的情况
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res, s = 0, 0
        seen = {0: 0}
        for i, n in enumerate(nums):
            s = s + 1 if n == 1 else s - 1
            if s in seen:
                res = max(res, i - seen[s] if s != 0 else i + 1)
            else:
                seen[s] = i
        return res


def test_case(nums: List[int]) -> int:
    s = Solution()
    return s.findMaxLength(nums)
