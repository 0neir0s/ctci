class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchFromTopRight(row, col):
            if row == R or col == -1:
                return False
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                return searchFromTopRight(row, col-1)
            else:
                return searchFromTopRight(row+1, col)   
        R, C = len(matrix), len(matrix[0])
        return searchFromTopRight(0,C-1)
