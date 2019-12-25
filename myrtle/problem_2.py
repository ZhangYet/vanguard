class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        seen = {s[0]: 0}
        max_len = 1

        for idx, value in enumerate(s[1:], 1):
            if value in seen:
                print(f'idx changed to {idx}')
                i = idx

            max_len = max(max_len, idx - i + 1)
            seen[value] = idx
            print(f'seen: {seen}, value: {value}, iter: ({idx}, {i}), max_len: {max_len}')

        return max_len


def test_solution(s: str):
    sol = Solution()
    return sol.lengthOfLongestSubstring(s)

