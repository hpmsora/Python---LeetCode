class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        prev_prev_prev_num = 0
        prev_prev_num = 1
        prev_num = 1
        
        index = 3
        
        while index <= n:
            curr_num = prev_prev_prev_num + prev_prev_num + prev_num
            prev_prev_prev_num = prev_prev_num
            prev_prev_num = prev_num
            prev_num = curr_num
            index += 1
        return curr_num