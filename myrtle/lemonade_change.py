# https://leetcode.com/problems/lemonade-change/

from typing import List
from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True

        if bills[0] != 5:
            return False

        changas = defaultdict(int)
        def pay_changa(bill: int) -> bool:
            if bill == 5:
                changas[bill] += 1
                return True

            if bill == 10:
                if changas[5] < 1:
                    return False
                changas[5] -= 1
                changas[10] += 1
                return True

            if bill == 20:
                if changas[10] >= 1 and changas[5] >= 1:
                    changas[10] -= 1
                    changas[5] -= 1
                    return True

                if changas[5] >= 3:
                    changas[5] -= 3
                    return True

                return False
        for bill in bills:
            if not pay_changa(bill):
                return False
        return True


