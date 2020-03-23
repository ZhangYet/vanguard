package goal

func inOrderForThisProblem(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	left := inOrderForThisProblem(root.Left)
	left = append(left, root.Val)
	right := inOrderForThisProblem(root.Right)
	left = append(left, right...)
	return left
}

func isValidBST(root *TreeNode) bool {
	nums := inOrderForThisProblem(root)
	if len(nums) <= 1 {
		return true
	}
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] >= nums[i+1] {
			return false
		}
	}
	return true
}
