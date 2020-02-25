# https://leetcode.com/problems/unique-binary-search-trees/

# base on
# https://leetcode.com/problems/unique-binary-search-trees/discuss/462118/C%2B%2B-faster-than-100-less-memory-than-65.91


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        ret = [0] * (n + 1)
        ret[0] = ret[1] = 1
        for i in range(2, n + 1):
            idx_half = i // 2
            for j in range(0, idx_half):
                ret[i] += 2 * (ret[j] * ret[i - j - 1])
            if i % 2:
                ret[i] += ret[idx_half] * ret[idx_half]
        return ret[n]


def test_solution(n):
    s = Solution()
    return s.numTrees(n)