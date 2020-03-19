package goal

// 问题在于记录父节点

func search(target, level int, node *TreeNode) (*TreeNode, int) {
	if node == nil {
		return node, -1
	}

	if (node.Left != nil && node.Left.Val == target) || (node.Right != nil && node.Right.Val == target) {
		return node, level + 1
	}
	if target < node.Val {
		return search(target, level+1, node.Left)
	}
	if target > node.Val {
		return search(target, level+1, node.Right)
	}
	return node, -1
}

func isCousins(root *TreeNode, x int, y int) bool {
	if root.Val == x || root.Val == y {
		return false
	}
	xp, xlevel := search(x, 0, root)
	yp, ylevel := search(y, 0, root)
	return xlevel > 0 && ylevel > 0 && xlevel == ylevel && yp != xp

}
