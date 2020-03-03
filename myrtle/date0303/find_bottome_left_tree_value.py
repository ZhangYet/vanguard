# https://leetcode.com/problems/find-bottom-left-tree-value/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        from collections import deque

        queue = deque([root])
        left_most = root.val

        while queue:
            left_most = queue[-1].val
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.left)
        return left_most
