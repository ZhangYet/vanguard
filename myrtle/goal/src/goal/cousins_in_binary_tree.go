package goal

// 问题在于记录父节点
// 居然还不是二叉搜查树g

func search(target, level int, cur, prev *TreeNode) (*TreeNode, int) {
	if cur == nil {
		return nil, -1
	}
	if cur.Val == target {
		return prev, level
	}

	res, level := search(target, level+1, cur.Left, cur)
	if res != nil {
		return res, level
	}
	return search(target, level+1, cur.Right, cur)
}

func isCousins(root *TreeNode, x int, y int) bool {
	if root.Val == x || root.Val == y {
		return false
	}
	xp, xlevel := search(x, 0, root, nil)
	yp, ylevel := search(y, 0, root, nil)
	return xlevel > 0 && ylevel > 0 && xlevel == ylevel && yp != xp
}
