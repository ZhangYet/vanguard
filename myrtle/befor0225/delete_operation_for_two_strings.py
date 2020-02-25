# https://leetcode.com/problems/delete-operation-for-two-strings/
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        len_word1 = len(word1)
        len_word2 = len(word2)
        if not word1 or not word2:
            return len_word1 + len_word2

        distance: List[List[int]] = [[0] * len_word2 for _ in range(len_word1)]
        print(f"init distance: {distance}")

        flag1 = False
        for i in range(len_word2):
            if word2[i] == word1[0] or flag1:
                distance[0][i] = 1
                flag1 = True
                print(
                    f"update row0 i: {i}, word1[0]: {word1[0]}, word2[i]: {word2[i]} -- {distance}"
                )
            else:
                distance[0][i] = 0
        print(f"after row0: {distance}")

        flag2 = False
        for j in range(len_word1):
            if word1[j] == word2[0] or flag2:
                distance[j][0] = 1
                flag2 = True
                print(
                    f"update col0, j: {j}, word1[j]: {word1[j]}, word2[0]: {word2[0]} -- {distance}"
                )
            else:
                distance[j][0] = 0

        print(f"after col0: {distance}")

        for row in range(1, len_word1):
            for col in range(1, len_word2):
                distance[row][col] = max(distance[row - 1][col], distance[row][col - 1])
                if word1[row] == word2[col]:
                    distance[row][col] = max(
                        distance[row][col], distance[row - 1][col - 1] + 1
                    )

        return len_word1 + len_word2 - 2 * distance[len_word1 - 1][len_word2 - 1]


def test_case(s1: str, s2: str):
    i = Solution()
    return i.minDistance(s1, s2)
