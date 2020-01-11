# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        nrows = len(matrix)
        ncols = len(matrix[0])

        if not ncols:
            return False

        row, col = 0, ncols - 1
        while row < nrows and col >= 0:
            print(f'{row}, {col}: {matrix[row][col]}')
            curr = matrix[row][col]
            if curr == target:
                return True
            if curr > target:
                col -= 1
            if curr < target:
                row += 1

        return False



