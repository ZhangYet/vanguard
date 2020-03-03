# https://leetcode.com/problems/buddy-strings/
# 感觉这道题是 https://leetcode.com/problems/k-similar-strings/ 的基础，所以做一下
# class Solution:
#     def buddyStrings(self, A: str, B: str) -> bool:
#         len_a = len(A)
#         len_b = len(B)
#
#         if len_a != len_b:
#             return False
#
#         if len_a <= 1:
#             return False
#
#         from collections import Counter
#
#         counter_a = Counter(A)
#         counter_b = Counter(B)
#         if counter_a != counter_b:
#             return False
#
#         diff = 0
#         for i in range(len_a):
#             if B[i] not in counter_a:
#                 return False
#             if B[i] != A[i]:
#                 diff += 1
#                 if diff > 2:
#                     return False
#
#         if diff == 2:
#             return True
#
#         if diff == 0:
#             for k, v in counter_a.items():
#                 if v > 1:
#                     return True
#
#             return False
#
#         return False


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2:
            return False
        from collections import Counter

        if A == B and Counter(A).most_common()[0][1] > 1:
            return True

        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)

        return (
            (A[diff[0]], A[diff[1]]) == (B[diff[1]], B[diff[0]])
            if len(diff) == 2
            else False
        )
