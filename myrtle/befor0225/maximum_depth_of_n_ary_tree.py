from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0

        def _depth(node: Node) -> int:
            if not node.children:
                return 1

            return max([_depth(n) for n in node.children]) + 1

        return _depth(root)
