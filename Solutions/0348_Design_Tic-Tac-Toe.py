class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.isWin = 0

    def move(self, row: int, col: int, player: int) -> int:
        if self.isWin == 0 or self.matrix[row][col] == 0:
            if player == 1:
                self.matrix[row][col] = 1
            if player == 2:
                self.matrix[row][col] = -1
        self.isWin = self.winCheck()
        return self.isWin
        
    # 1: player 1 win
    # 2: player 2 win
    # 0: no win
    def winCheck(self) -> int:
        # row check
        for each_row in self.matrix:
            r_sum = sum(each_row)
            if r_sum == self.n:
                return 1
            elif r_sum == -1*self.n:
                return 2
        
        # column check
        for index in range(self.n):
            c_sum = sum([self.matrix[x][index] for x in range(self.n)])
            if c_sum == self.n:
                return 1
            elif c_sum == -1 * self.n:
                return 2
        
        # diagonal check
        sum_1 = 0
        sum_2 = 0
        for index in range(self.n):
            sum_1 += self.matrix[index][index]
            sum_2 += self.matrix[self.n - index - 1][index]
        
        if sum_1 == self.n or sum_2 == self.n:
            return 1
        elif sum_1 == -1*self.n or sum_2 == -1*self.n:
            return 2
        
        # RETURN
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)