# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List

class Solution:
    def preorder(self, root: Node) -> List[int]:

        def _preorder(node: Node):
            if not node:
                return

            res = [node.val]
            for x in _preorder(node.children):
                for y in x:
                    res.append(y)
            return res

        return _preorder(root)
