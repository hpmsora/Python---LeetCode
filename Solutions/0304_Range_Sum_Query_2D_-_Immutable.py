class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = matrix
        
        for index_m in range(m):
            row_sum = 0
            for index_n in range(n):
                each_sum = 0
                row_sum += self.matrix[index_m][index_n]
                if index_m > 0:
                    each_sum += self.matrix[index_m-1][index_n]
                each_sum += row_sum
                self.matrix[index_m][index_n] = each_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sol = self.matrix[row2][col2]
        if row1 > 0:
            sol -= self.matrix[row1 - 1][col2]
        if col1 > 0:
            sol -= self.matrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            sol += self.matrix[row1 - 1][col1 - 1]
            
        return sol


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)