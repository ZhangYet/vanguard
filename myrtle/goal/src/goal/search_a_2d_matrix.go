package goal

// https://leetcode.com/problems/search-a-2d-matrix-ii/

func searchMatrix(matrix [][]int, target int) bool {
	nRows := len(matrix)
	if nRows <= 0 {
		return false
	}
	nCols := len(matrix[0])
	if nCols <= 0 {
		return false
	}

	rowIndex, colIndex := 0, nCols-1
	for {
		if rowIndex < nRows && colIndex >= 0 {
			if matrix[rowIndex][colIndex] == target {
				return true
			}
			if matrix[rowIndex][colIndex] < target {
				rowIndex += 1
				continue
			}
			if matrix[rowIndex][colIndex] > target {
				colIndex -= 1
				continue
			}
		}
		return false
	}
}
