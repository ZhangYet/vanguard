# https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque

        stack = deque([root])
        res = []
        while stack:
            new_stack = []
            values = []
            while stack:
                cur = stack.popleft()
                values.append(cur.val)
                if cur.left:
                    new_stack.append(cur.left)
                if cur.right:
                    new_stack.append(cur.right)

            res.append(values)
            stack = deque(new_stack)

        return res
