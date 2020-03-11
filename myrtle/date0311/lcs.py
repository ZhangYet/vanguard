# https://leetcode.com/problems/longest-common-subsequence/
# 写一个节省空间的 DP 吧，只用一维数组
# 失败了


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        rows, cols = text1, text2
        if len(text1) > len(text2):
            rows, cols = text2, text1
        row_num, col_num = len(rows), len(cols)
        res = [0] * row_num

        for row in range(row_num):
            print(f"row: {row}, res: {res}")
            for col in range(col_num):
                if row == 0:
                    if rows[row] == cols[col]:
                        res[row] = 1
                    res[row] = max(res[row], 0)
                    continue

                res[row] = max(res[row - 1], res[row])
                if rows[row] == cols[col]:
                    res[row] = max(res[row], res[row - 1] + 1)
        return res[-1]


def test_case(text1="ezupkr", text2="ubmrapg"):
    s = Solution()
    return s.longestCommonSubsequence(text1, text2)
