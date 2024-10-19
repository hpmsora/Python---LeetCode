class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        one_iter = (numRows-1)*2

        group_iter = {}

        for i in range(one_iter//2 +1):
            group_iter[i] = i
            group_iter[one_iter - i] = i

        sol_list = [""] * numRows

        for index, each_s in enumerate(s):
            mod = index % one_iter
            group = group_iter[mod]
            sol_list[group] += each_s
        
        return ''.join(sol_list)