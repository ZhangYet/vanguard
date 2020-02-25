# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.depth = 0

        def _depth(root: TreeNode, level):
            if not root:
                return

            self.depth = max(level, self.depth)
            _depth(root.left, level+1)
            _depth(root.right, level+1)

        _depth(root, 1)
        return self.depth
