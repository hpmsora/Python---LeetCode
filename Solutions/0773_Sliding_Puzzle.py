class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        zero_move_dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        board_str =  ""

        zero_index = 0
        index = 0
        for each_m in board:
            for each_n in each_m:
                board_str += str(each_n)
                if each_n == 0:
                    zero_index = index
                index += 1

        vistied_board = set([board_str])

        queue = collections.deque([(board_str, zero_index, 0)])

        sol = 0
        target = "123450"

        while queue:
            curr_board, zero_index, step = queue.popleft()

            if curr_board == target:
                return step
            
            for each_zero_move_dirs in zero_move_dirs[zero_index]:
                temp_curr_board = list(curr_board)

                temp_curr_board[zero_index], temp_curr_board[each_zero_move_dirs] = temp_curr_board[each_zero_move_dirs], temp_curr_board[zero_index]
                temp_curr_board = ''.join(temp_curr_board)
                if not temp_curr_board in vistied_board:
                    queue.append((temp_curr_board, each_zero_move_dirs, step + 1))
                    vistied_board.add(temp_curr_board)
        
        return -1