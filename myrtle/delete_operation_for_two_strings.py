# https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        if not word1:
            return len(word2)

        if not word2:
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])

        return 1 + min(
            self.minDistance(word1[1:], word2),
            self.minDistance(word1[:-1], word2),
            self.minDistance(word2[1:], word1),
            self.minDistance(word2[:-1], word1),
        )


def test_case(s1: str, s2: str):
    i = Solution()
    return i.minDistance(s1, s2)
