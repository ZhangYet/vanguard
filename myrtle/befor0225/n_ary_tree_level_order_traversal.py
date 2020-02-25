from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []

        next_level_stack = root.children
        res = [[root.val]]

        while next_level_stack:
            new_next_level = []
            cur_values = []
            for node in next_level_stack:
                new_next_level += node.children
                cur_values.append(node.val)
            res.append(cur_values)
            next_level_stack = new_next_level

        return res

