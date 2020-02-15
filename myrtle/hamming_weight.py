class Solution:
    def hammingWeight(self, n: int) -> int:
        s = n & 1
        cur = n >> 1
        while cur:
            s += cur & 1
            cur >>= 1

        return s


def test_case():
    s = Solution()
    assert s.hammingWeight(3) == 2
    assert s.hammingWeight(4) == 1
