class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        new_matrix = [[0]*n for i in range(n)]

        # Upside-Down reverse
        for index in range(n):
            new_matrix[index] = matrix[n - index - 1][:]
        
        # Transpose
        for i in range(n):
            for j in range(n):
                matrix[j][i] = new_matrix[i][j]