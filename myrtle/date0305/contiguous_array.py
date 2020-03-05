# https://leetcode.com/problems/contiguous-array/
# 看起来还挺麻烦的，想不到 DP 解法
# 如果我们创建一个累积有多少1的数组，会不会有帮助？
# 主要是怎样判断我们找到最大了？
# 怎样处理那些前面有太多0的情况？
# 试试用类似 DP 的算法吧
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        matrix = [[] for _ in nums]
        for row in range(len(nums)):
            for col in range(len(nums)):
                if row > col:
                    matrix[row].append(())
                    continue

                if row == 0:
                    matrix[row].append(
                        (
                            sum(nums[row : (col + 1)]),
                            col - row + 1 - sum(nums[row : col + 1]),
                        )
                    )
                    continue

                up_level = matrix[row - 1][col]
                if nums[row - 1] == 1:
                    matrix[row].append((up_level[0] - 1, up_level[1]))
                else:
                    matrix[row].append((up_level[0], up_level[1] - 1))

        res = 0
        for row in range(len(nums)):
            for col in range(len(nums)):
                if not matrix[row][col]:
                    continue
                data = matrix[row][col]
                if data[1] == data[0]:
                    res = max(res, col - row + 1)
        from utils import print_matrix

        print_matrix(matrix)
        return res


def test_case(nums: List[int]) -> int:
    s = Solution()
    return s.findMaxLength(nums)
