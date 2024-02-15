class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n_row = len(mat) # num of row
        n_col = len(mat[0]) # num of column

        # List reserve List[List[int]]
        sol_list = []

        # start with top row
        for row in range(n_row):
            temp_list = []
            for col in range(n_col):
                if row < 0:
                    break
                temp_list = [mat[row][col]] + temp_list
                row -= 1
            sol_list.append(temp_list)
        
        # start with right column
        for col in range(1, n_col):
            temp_list = []
            for row in range(n_row):
                if col >= n_col:
                    break
                temp_list = [mat[n_row - row - 1][col]] + temp_list
                col += 1
            sol_list.append(temp_list)

        # organize sol_list
        sol = []
        isReversed = True
        for each_sol_list in sol_list:
            if isReversed:
                sol += each_sol_list[::-1]
            else:
                sol += each_sol_list
            isReversed = isReversed == False
        return sol