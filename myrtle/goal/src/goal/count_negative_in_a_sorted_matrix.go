package goal

// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
// TODO: 尝试从右边开始看看会不会快点

func countNegatives(grid [][]int) int {
	rows := len(grid)
	if rows <= 0 {
		return 0
	}
	cols := len(grid[0])
	if cols <= 0 {
		return 0
	}
	count := 0
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if grid[row][col] < 0 {
				count += cols - col
				break
			}
		}
	}
	return count
}
