# https://leetcode.com/problems/edit-distance/
# 神作，在 leetcode 里面 summit 跟 run 的结果不同，在本地


class Solution:
    cache = {}

    def minDistance(self, word1: str, word2: str) -> int:
        def edist(i, j) -> int:
            if (i, j) in self.cache:
                return self.cache[(i, j)]

            if i == len(word1):
                return max(0, len(word2) - j)

            if j == len(word2):
                return max(0, len(word1) - i)

            if word1[i] == word2[j]:
                d = edist(i + 1, j + 1)
                self.cache[(i, j)] = d
                return d
            else:
                d_replace = edist(i + 1, j + 1) + 1
                d_delete = edist(i + 1, j) + 1
                d_insert = edist(i, j + 1) + 1
                res = min(d_replace, d_delete, d_insert)
                self.cache[(i, j)] = res
                return res

        return edist(0, 0)


def test_case(word1: str, word2: str) -> int:
    s = Solution()
    return s.minDistance(word1, word2)
