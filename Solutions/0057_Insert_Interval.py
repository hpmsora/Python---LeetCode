class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        sol_index = []
        new_start = n_start
        new_end = n_end
        cut_index = 0
        isLast = True
        for index in range(len(intervals)):
            start, end = intervals[index]
            if start > n_end:
                cut_index = index
                isLast = False
                break
            elif end < n_start:
                continue
            sol_index.append(index)
            new_start = min([new_start, start])
            new_end = max([new_end, end])
        if isLast:
            cut_index = len(intervals) - 1
        if sol_index:
            intervals[sol_index.pop(0)] = [new_start, new_end]
            if sol_index:
                pop_index = sol_index[0]
                for _ in sol_index:
                    intervals.pop(pop_index)
        else:
            if isLast:
                intervals.append(newInterval)
            elif cut_index == 0:
                intervals = [newInterval] + intervals
            else:
                intervals = intervals[:cut_index] + [newInterval] + intervals[cut_index:]
        return intervals