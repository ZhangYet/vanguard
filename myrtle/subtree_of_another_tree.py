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

        s_str = preorder(s)
        t_str = preorder(t)
        return t in s_str