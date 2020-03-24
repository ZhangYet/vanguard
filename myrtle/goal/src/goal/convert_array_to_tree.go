package goal

// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	if len(nums) == 1 {
		return &TreeNode{Val: nums[0]}
	}
	mid := len(nums) / 2
	root := &TreeNode{Val: mid}
	root.Left = sortedArrayToBST(nums[:mid])
	root.Right = sortedArrayToBST(nums[mid+1:])
	return root
}

/* 我寻思我就是跟正确答案没啥不同呀？
func sortedArrayToBST(nums []int) *TreeNode {
	n := len(nums)
	if n == 0{
		return nil
	}
	if n == 1{
		return &TreeNode{
			Val : nums[0],
		}
	}
	m := n / 2
	return &TreeNode{
		Val : nums[m],
		Left : sortedArrayToBST(nums[:m]),
		Right : sortedArrayToBST(nums[m + 1 :]),
	}

}
*/
