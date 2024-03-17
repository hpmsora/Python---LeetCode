class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        new_start, new_end = newInterval

        index = 0
        start_index = float("inf")
        end_index = float("-inf")
        new_start_int = new_start
        new_end_int = new_end

        for start, end in intervals:
            isValid = False
            if start <= new_start and new_start <= end: # Start point check
                isValid = True
            elif start <= new_end and new_end <= end:
                isValid = True
            elif new_start <= start and start <= new_end:
                isValid = True
            elif new_start <= end and end <= new_end:
                isValid = True
            elif new_end < start:
                break

            if isValid:
                start_index = min(start_index, index)
                end_index = max(end_index, index)

                new_start_int = min(new_start_int, start)
                new_end_int = max(new_end_int, end)
                print(start_index)

            index += 1

        newInterval_final = [new_start_int, new_end_int]

        if index == 0 and start_index == float("inf"):
            sol = [[new_start_int, new_end_int]] + intervals
        elif index == len(intervals) and start_index == float("inf"):
            sol = intervals + [[new_start_int, new_end_int]]
        elif start_index == float("inf"):
            sol = intervals[:index] + [[new_start_int, new_end_int]] + intervals[index:]
        else:
            sol = intervals[:start_index] + [[new_start_int, new_end_int]] + intervals[end_index + 1:]

        return sol