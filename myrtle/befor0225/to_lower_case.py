# https://leetcode.com/problems/to-lower-case/
class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([c.lower() if c <= "Z" else c for c in str])
