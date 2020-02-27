# https://leetcode.com/problems/merge-two-binary-trees/
# 感觉单纯递归就可以了
# 如果不想创建新的树，可以在原来的树上面想办法，不过终止条件会麻烦一点


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2

        if not t2:
            return t1

        def _merge_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
            if not t1:
                return t2

            if not t2:
                return t1

            node = TreeNode(t1.val + t2.val)
            node.left = _merge_trees(t1.left, t2.left)
            node.right = _merge_trees(t1.right, t2.right)
            return node

        return _merge_trees(t1, t2)


# 想不到还挺快的
