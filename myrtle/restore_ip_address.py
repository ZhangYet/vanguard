# https://leetcode.com/problems/restore-ip-addresses/

from typing import List


def lstrim_zero(s: str):
    tmp = s.lstrip('0')
    if len(tmp) > 0:
        return tmp
    return '0'

def is_valid_sec(s: str):
    if not s:
        return False
    try:
        return 0 <= int(s) and int(s) <= 255
    except ValueError:
        print(f'parse error: {s}')
        return False


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:

        def parse(s: str, n: int) -> List[str]:
            if n == 1:
                clean_s = lstrim_zero(s)
                print(f'the last session: {s}, {clean_s}')
                if is_valid_sec(clean_s):
                    return [clean_s]
                else:
                    return []
            res = []
            if is_valid_sec(s[:1]):
                res += [s[:1] + '.' + x for x in parse(s[1:], n-1)]

            clean_h2 = lstrim_zero(s[:2])
            if is_valid_sec(clean_h2):
                res += [clean_h2 + '.' + x for x in parse(s[2:], n-1)]

            clean_h3 = lstrim_zero(s[:3])
            if is_valid_sec(clean_h3):
                res += [clean_h3 + '.' + x for x in parse(s[3:], n-1)]

            return res

        return list(set(parse(s, 4)))


def test_case(s: str):
    sol = Solution()
    return sol.restoreIpAddresses(s)
