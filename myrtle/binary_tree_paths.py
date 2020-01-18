# https://leetcode.com/problems/binary-tree-paths/

class TreeNode:
    def __init__(self, x: str):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def paths(root: TreeNode) -> List[str]:
            if not root:
                return []

            print(f'root.val: {root.val}')

            if not root.left and not root.right:
                return [root.val]

            if not root.right:
                return [root.val + '->' + x for x in paths(root.left)]

            if not root.left:
                return [root.val + '->' + x for x in paths(root.right)]

            return [root.val + '->' + x for x in paths(root.left)] + \
                [root.val + '->' + x for x in paths(root.right)]

        return paths(root)

def test_case():
    n1 = TreeNode('1')
    n2 = TreeNode('2')
    n3 = TreeNode('3')
    n1.left = n2
    n1.right = n3
    return n1



