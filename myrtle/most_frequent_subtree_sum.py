# https://leetcode.com/problems/most-frequent-subtree-sum/
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return [0]

        self.record = {}

        def _tree_sum(root: TreeNode):
            if not root:
                return 0

            s = root.val + _tree_sum(root.left) + _tree_sum(root.right)
            if s not in self.record:
                self.record[s] = 0
            self.record[s] += 1
            return s

        _tree_sum(root)
        items = list(self.record.items())
        sorted(items, key=lambda x: x[1], reverse=True)
        return [x[0] for x in items if x[1] == items[-1][1]]

