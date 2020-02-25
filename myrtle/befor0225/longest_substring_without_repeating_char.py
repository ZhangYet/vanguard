class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_so_far = current_max = init = 0
        record = {}

        for idx, value in enumerate(s):
            if value in record and record[value] >= init:
                init = record[value] + 1  # update left
                max_so_far = max(max_so_far, current_max)  # save max_so_far
                current_max = idx - record[value]  # update current_max
            else:
                current_max += 1

            record[value] = idx

        return max(max_so_far, current_max)


def test_solution(s: str):
    sol = Solution()
    return sol.lengthOfLongestSubstring(s)
