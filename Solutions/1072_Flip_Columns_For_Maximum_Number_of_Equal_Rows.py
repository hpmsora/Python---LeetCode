class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_dict = {}
        sol = 0

        for each_matrix in matrix:
            if each_matrix[0] == 0:
                raw_each_matrix = ''.join(str(x) for x in each_matrix)
            else:
                raw_each_matrix = ''.join(str((x+1)%2) for x in each_matrix)

            if raw_each_matrix in row_dict:
                row_dict[raw_each_matrix] += 1
            else:
                row_dict[raw_each_matrix] = 1
            sol = max(sol, row_dict[raw_each_matrix])
        
        return sol