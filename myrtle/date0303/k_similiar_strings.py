# https://leetcode.com/problems/k-similar-strings
# 据说可以用 BFS
# 好巧妙，其实就是把每次 swap 之后的字符串作为新的节点
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        record = {}

        def swap(s: str, i: int, j: int) -> str:
            l = list(s)
            l[i], l[j] = l[j], l[i]
            return "".join(l)

        def f(curr: str, index: int, target: str) -> int:
            if curr == B:
                return 0
            if curr in record:
                return record[curr]

            while index < len(target) and target[index] == curr[index]:
                index += 1

            ans = 65535
            for i in range(index + 1, len(target)):
                if curr[i] == target[index]:
                    buffer = swap(curr, i, index)
                    ans = min(ans, f(buffer, index, target))
            record[curr] = 1 + ans
            return 1 + ans

        return f(A, 0, B)


def test_case(A: str, B: str) -> int:
    s = Solution()
    return s.kSimilarity(A, B)


def wrong_case():
    A = "bccaba"
    B = "abacbc"
    return test_case(A, B)
