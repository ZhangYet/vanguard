# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            new_queue = []
            cur_level = []
            while queue:
                cur = queue.pop()
                cur_level.append(cur.val)
                if cur.left:
                    new_queue.append(cur.left)
                if cur.right:
                    new_queue.append(cur.right)

            res.append(max(cur_level))
            if not new_queue:
                break
            queue = new_queue
        return res
    
