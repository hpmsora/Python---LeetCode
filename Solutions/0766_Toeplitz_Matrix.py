class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])

        # Upper triagle
        for index_col in range(n_col):
            num = matrix[0][index_col]

            col = index_col
            row = 0

            while col < n_col and row < n_row:
                sub_num = matrix[row][col]
                if not num == sub_num:
                    return False
                col += 1
                row += 1
        # Lower Triangle
        for index_row in range(1, n_row):
            num = matrix[index_row][0]

            col = 0
            row = index_row

            while col < n_col and row < n_row:
                sub_num = matrix[row][col]
                if not num == sub_num:
                    return False
                col += 1
                row += 1

        return Truev