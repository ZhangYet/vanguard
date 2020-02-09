from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        self.res = []

        def find_largest_each_row(row: List[TreeNode]):
            if all([x is None for x in row]):
                return

            values = [x.val for x in row]
            self.res.append(max(values))

            next_level = [x.left for x in row if x.left] + [
                x.right for x in row if x.right
            ]
            return find_largest_each_row(next_level)

        find_largest_each_row([root])
        return self.res
