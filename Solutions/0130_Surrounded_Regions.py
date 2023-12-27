class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def recurr(board, m, n, pos_x, pos_y):
            if pos_y > 0:
                if board[pos_y - 1][pos_x] == "O":
                    board[pos_y - 1][pos_x] = "I"
                    board = recurr(board, m, n, pos_x, pos_y - 1)
            if pos_y < n-1:
                if board[pos_y + 1][pos_x] == "O":
                    board[pos_y + 1][pos_x] = "I"
                    board = recurr(board, m, n, pos_x, pos_y + 1)
            if pos_x > 0:
                if board[pos_y][pos_x - 1] == "O":
                    board[pos_y][pos_x - 1] = "I"
                    board = recurr(board, m, n, pos_x - 1, pos_y)
            if pos_x < m-1:
                if board[pos_y][pos_x + 1] == "O":
                    board[pos_y][pos_x + 1] = "I"
                    board = recurr(board, m, n, pos_x + 1, pos_y)
            return board
        
        m = len(board[0])
        n = len(board)

        boundary_indices = set()

        for each_m in range(m):
            boundary_indices.add((each_m, 0))
            boundary_indices.add((each_m, n-1))
        for each_n in range(n):
            boundary_indices.add((0, each_n))
            boundary_indices.add((m-1, each_n))
        boundary_indices = list(boundary_indices)

        for each_x, each_y in boundary_indices:
            if board[each_y][each_x] == "O":
                board[each_y][each_x] = "I"
                board = recurr(board, m, n, each_x, each_y)

        for i in range(m):
            for j in range(n):
                if board[j][i] == "O":
                    board[j][i] = "X"
                elif board[j][i] == "I":
                    board[j][i] = "O"