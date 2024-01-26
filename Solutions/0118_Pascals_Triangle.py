class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [[1]]
        for index in range(1, numRows):
            temp_sol = []
            n_element = index + 1
            prev_sol = sol[-1]
            for sub_index in range(n_element):
                if sub_index == 0:
                    num = 1
                elif sub_index == n_element - 1:
                    num = 1
                else:
                    num = prev_sol[sub_index-1] + prev_sol[sub_index]
                temp_sol.append(num)
            sol.append(temp_sol)
        return sol