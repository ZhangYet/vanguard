# https://leetcode.com/problems/find-duplicate-subtrees/
# 这道题看起来比较难啊，因为要比较的子树太多了。
# 话说如果可以从叶节点比较起来，倒是方便，但是我们不能加指针啊。
# 能不能通过遍历，将所有子树对应的 key 记录起来？不太行，因为要记录 key 本身就要遍历一次子树
# 啊其实可以通过找 pattern 找到对应的重复 root，然后再遍历一次把值等于对应的 root 找出来
# 但这其实有个问题，你不知道这个 pattern 是不是同一个子树的，我觉得可以通过用 # 表示空子树来处理
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_order(root: TreeNode) -> str:
    if not root:
        return "#"

    return f"{in_order(root.left)}{root.val}{in_order(root.right)}"


def find_dup_pattern(s: str) -> List[str]:
    import re
    from collections import Counter

    res = []
    for i in range(1, len(s) // 2):
        p = r"\d{{{}}}#".format(i)
        patterns = re.findall(p, s)
        c = Counter(patterns)
        for k, v in c.items():
            if v > 1:
                res.append(k)
    return res


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        pattern_str = in_order(root)
        patterns = find_dup_pattern(pattern_str)
        if not patterns:
            return []

        root_values = set([int(s[0]) for s in patterns])

        self.res: List[TreeNode] = []

        def _in_order(root: TreeNode):
            if not root:
                return

            if root.val in root_values:
                self.res.append(root)
                root_values.remove(root.val)

            _in_order(root.left)
            _in_order(root.right)

        _in_order(root)
        return self.res


def test_case():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    p = in_order(root)

    s = Solution()
    return s.findDuplicateSubtrees(root)
