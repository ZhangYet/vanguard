# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# 因为每个 chars 中的字母都只能用一次，所以还是有点难度的
# 先 count 一下吧
# 也没有这么简单，每个词也需要 count
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter

        cs = Counter(chars)
        res = 0
        for word in words:
            wc = Counter(word)
            found = True
            for k, v in wc.items():
                if k not in cs:
                    found = False
                    break
                if cs[k] - wc[k] < 0:
                    found = False
                    break
            if found:
                res += len(word)

        return res


wtf = [
    "dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
    "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
    "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
    "boygirdlggnh",
    "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
    "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
    "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
    "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
    "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
    "oxgaskztzroxuntiwlfyufddl",
    "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
    "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
    "eeilfdaookieawrrbvtnqfzcricvhpiv",
    "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
    "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
    "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
    "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo",
    "teyygdmmyadppuopvqdodaczob",
    "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
    "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs",
]
chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"


def test_case():
    s = Solution()
    assert s.countCharacters(wtf, chars) == 0
    assert s.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6
