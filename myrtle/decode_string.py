# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
                continue

            partial_str = ""
            while stack[-1] != "[":
                partial_str += stack.pop()
            stack.pop()

            partial_str = partial_str[::-1]

            count = 0
            level = 0
            while stack:
                if not stack[-1].isdigit():
                    break
                count += pow(10, level) * int(stack.pop())
                level += 1

            cur_str = partial_str * count
            stack.extend(cur_str)

        return "".join(stack)


def test_case():
    s = Solution()
    r = s.decodeString("3[a2[c]]")
    print(r)
    assert r == "accaccacc"
̊