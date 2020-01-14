# https://leetcode.com/problems/tag-validator/submissions/

class Tag:

    def __init__(self, tag_name: str, is_closed: bool):
        self.tag_name = tag_name
        self.is_closed = is_closed

    def valid_tag_name(self) -> bool:
        if len(self.tag_name) > 9:
            return False
        if self.tag_name.upper() != self.tag_name:
            return False
        return True

class Solution:
    def isValid(self, code: str) -> bool:
        if not code:
            return True

        tags_stack = []
        new_tag = None

        i = 0
        L = len(code)
        while i < L:
            if code[i] == '<' and new_tag:
                return False

            if code[i] == '>' and not new_tag:
                i += 1
                pass

            if code[i] == '<':
                new_tag = Tag('', code[i+1] == '/')
                i += 2
                continue

            if code[i] == '>':
                if not new_tag.valid_tag_name():
                    return False

                if new_tag.is_closed:
                    open_tag: Tag = tags_stack.pop()
                    if open_tag.tag_name != new_tag.tag_name:
                        return False

                tags_stack.append(new_tag)
                new_tag = None

            new_tag.tag_name += code[i]

            i += 1

        return True


def test_case(s: str):
    i = Solution()
    return i.isValid(s)
