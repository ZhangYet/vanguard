package goal

// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
// 直接的解法就是取两个树的值，然后合并排序。
// 好一点的方法就是先中序遍历，这样两个 array 是有序的

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inOrder(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	left := inOrder(root.Left)
	left = append(left, root.Val)
	right := inOrder(root.Right)
	left = append(left, right...)
	return left
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	arr1 := inOrder(root1)
	arr2 := inOrder(root2)
	if len(arr1) == 0 {
		return arr2
	}
	if len(arr2) == 0 {
		return arr1
	}
	len1, len2 := len(arr1), len(arr2)
	res := []int{}
	i, j := 0, 0
	for {
		if i >= len1 && j >= len2 {
			break
		}
		if i >= len1 {
			res = append(res, arr2[j:]...)
			break
		}
		if j >= len2 {
			res = append(res, arr1[i:]...)
			break
		}
		if arr1[i] < arr2[j] {
			res = append(res, arr1[i])
			i += 1
		} else {
			res = append(res, arr2[j])
			j += 1
		}

	}

	return res
}
