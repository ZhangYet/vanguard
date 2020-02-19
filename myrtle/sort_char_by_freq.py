# https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        import heapq

        c = Counter(s)
        r = [(v, k) for k, v in c.items()]
        heapq.heapify(r)
        r.sort(reverse=True)
        return "".join([k * v for k, v in r])


def test_case(s: str):
    i = Solution()
    return i.frequencySort(s)
