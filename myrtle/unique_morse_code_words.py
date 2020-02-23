# https://leetcode.com/problems/unique-morse-code-words/
from typing import List


class Solution:
    alphabat = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]

    def translate(self, word: str) -> str:
        morse = [self.alphabat[ord(c) - ord("a")] for c in word]
        return "".join(morse)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res_list = [self.translate(w) for w in words]
        return len(set(res_list))
