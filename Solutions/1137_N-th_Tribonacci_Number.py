class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        num_list = [0, 1, 1]
        
        index = 3
        while index <= n:
            num_list.append(num_list[index-1] + num_list[index-2] + num_list[index-3])
            index += 1
        return num_list[-1]