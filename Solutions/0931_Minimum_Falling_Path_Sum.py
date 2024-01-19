class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #Initialization
        m = len(matrix)     # n row
        n = len(matrix[0])  # n column
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        # first row
        for index in range(n):
            dp[0][index] = matrix[0][index]
        
        # rest of row
        for row_index in range(1, m): # row iteration
            for col_index in range(n): # column iteration
                pre_list = []
                pre_list.append(dp[row_index-1][col_index])
                if not col_index == 0:
                    pre_list.append(dp[row_index-1][col_index - 1])
                if not col_index == n-1:
                    pre_list.append(dp[row_index-1][col_index + 1])
                dp[row_index][col_index] = min(pre_list) + matrix[row_index][col_index]
        # return
        return min(dp[-1])