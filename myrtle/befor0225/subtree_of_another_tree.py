# https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def _hash(val: int) -> int:
    return val * 50001299 % 50001377

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder(node: TreeNode) -> str:
            if not node:
                return '#'

            return f'{_hash(node.val)}{preorder(node.left)}{preorder(node.right)}'

        def inorder(node: TreeNode) -> str:
            if not node:
                return '#'

            return f'{inorder(node.left)}{_hash(node.val)}{inorder(node.right)}'

        def postorder(node: TreeNode) -> str:
            if not node:
                return '#'

            return f'{postorder(node.left)}{postorder(node.right)}{_hash(node.val)}'

        s_str = postorder(s)
        t_str = postorder(t)
        return t_str in s_str

# 只有 inorder 是不行的，奇怪