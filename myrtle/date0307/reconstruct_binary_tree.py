# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 这个思路是，predorder 的第一个 val 是子树的根节点
# 然后 inorder 可以用这个 val 划分出左子树和右子树
# 我们就这样递归下去即可
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        # left_pre = [v for v in preorder if v in inorder[:root_index]]
        # right_pre = [v for v in preorder if v in inorder[root_index + 1 :]]
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1 :])
        return root
