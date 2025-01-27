class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        sol = []

        for start, end in intervals:
            if sol:
                sol_start = sol[-1][0]
                sol_end = sol[-1][1]
                if sol_end < start:
                    sol.append([start, end])
                elif sol_start <= start and sol_end <= end:
                    sol[-1][0] = sol_start
                    sol[-1][1] = end
                elif sol_start <= start and end <= sol_end:
                    sol[-1][0] = sol_start
            else:
                sol.append([start, end])
        return sol