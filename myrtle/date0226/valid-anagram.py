# https://leetcode.com/problems/valid-anagram/
# 第一反应就是用一个 dict 记录并比较，但这未免太 trival 了
# 其实因为扩展里面提到如果是 unicode，就要想别的办法，所以我觉得还是用数组看起来合理一点（不过也没有多合理就是了）


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        record = [0] * 26
        for c in s:
            record[ord(c) - ord("a")] += 1

        for c in t:
            key = ord(c) - ord("a")
            record[key] -= 1
            if record[key] < 0:
                return False

        return True


# 干，最快的方法居然是就是数数（不过人家用 counter)
# ￿from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return  Counter(s) == Counter(t
