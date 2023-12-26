class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b_list = []
        for index_i in range(9):
            for index_j in range(9):
                num = board[index_i][index_j]
                if not num == ".":
                    b_list += [(index_i, num), (num, index_j), (index_i//3, index_j//3, num)]
        return len(b_list) == len(set(b_list))