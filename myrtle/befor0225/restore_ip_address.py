# https://leetcode.com/problems/restore-ip-addresses/

from typing import List


def is_valid_sec(s: str):
    if not s:
        return False
    if s == '0':
        return True
    if s.startswith('0'):
        return False

    return 1 <= int(s) and int(s) <= 255



class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:

        def parse(s: str, n: int) -> List[str]:
            if n == 1:
                if is_valid_sec(s):
                    return [s]
                else:
                    return []
            res = []
            if is_valid_sec(s[:1]):
                res += [f'{s[:1]}.{x}' for x in parse(s[1:], n-1)]

            if is_valid_sec(s[:2]):
                res += [f'{s[:2]}.{x}' for x in parse(s[2:], n-1)]

            if is_valid_sec(s[:3]):
                res += [f'{s[:3]}.{x}' for x in parse(s[3:], n-1)]

            return res

        return parse(s, 4)


def test_case(s: str):
    sol = Solution()
    return sol.restoreIpAddresses(s)
