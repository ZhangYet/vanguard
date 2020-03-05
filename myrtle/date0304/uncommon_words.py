# https://leetcode.com/problems/uncommon-words-from-two-sentences/
# 纯粹做来保持练习量
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter

        c = Counter((A + " " + B).split(" "))
        return [k for k, v in c.items() if v == 1]
