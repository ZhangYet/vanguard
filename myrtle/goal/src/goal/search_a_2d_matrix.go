package goal

// https://leetcode.com/problems/search-a-2d-matrix-ii/
// 从右上或者左下都有二分查找的效果
func searchMatrix(matrix [][]int, target int) bool {
	nRows := len(matrix)
	if nRows <= 0 {
		return false
	}
	nCols := len(matrix[0])
	if nCols <= 0 {
		return false
	}

	rowIndex, colIndex := nRows-1, 0
	for {
		if rowIndex >= 0 && colIndex < nCols {
			if matrix[rowIndex][colIndex] == target {
				return true
			}
			if matrix[rowIndex][colIndex] < target {
				colIndex += 1
				continue
			}
			if matrix[rowIndex][colIndex] > target {
				rowIndex -= 1
				continue
			}
		}
		return false
	}
}
