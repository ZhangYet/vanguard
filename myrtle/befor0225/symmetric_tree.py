# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        def _symmetric(left: TreeNode, right: TreeNode) -> bool:
            if (not left) and (not right):
                return True

            if not left or not right:
                return False

            return left.val == right.val and \
                _symmetric(left.left, right.right) and \
                _symmetric(left.right, right.left)

        return _symmetric(root.left, root.right)