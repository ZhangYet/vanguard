# https://leetcode.com/problems/generate-parentheses/
# 感觉可以递归解决
# 不太对，因为有多种情况，如果按照树的模式，那么就是指数式增长的了
# 所以需要剪枝
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        d = {1: {"()"}}
        for i in range(2, n + 1):
            d[i] = set([f"({x})" for x in d[i - 1]])

            for j in range(1, i // 2 + 1):
                k = i - j
                for x in d[j]:
                    for y in d[k]:
                        d[i].add(x + y)
                        d[i].add(y + x)

        return list(d[n])


def test_case(n: int) -> List[int]:
    s = Solution()
    return s.generateParenthesis(n)
