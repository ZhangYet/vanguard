#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque

        left_children = [root.val]
        stack = deque([root])

        while stack:
            cur = stack.popleft()
            if cur.right:
                stack.append(cur.right)
                left_children.append(cur.right.val)
            if cur.left:
                left_children.append(cur.left.val)
                stack.append(cur.left)

        return left_children[-1]
