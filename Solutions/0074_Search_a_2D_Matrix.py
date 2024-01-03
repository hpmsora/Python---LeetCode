class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index in range(len(matrix)):
            row = matrix[index]
            if row[0] > target:
                if index == 0:
                    return False
                else:
                    return target in matrix[index-1]
        return target in matrix[-1]