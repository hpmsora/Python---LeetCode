class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # Sort the points (ascending)
        points.sort()

        # Declare solution array
        sol = [points.pop(0)]

        # Loop - all points
        for start, end in points:
            # Declare solution iteration index
            sol_index = 0

            # Loop - all solution
            while sol_index < len(sol):

                # Get each solution range first
                sol_start, sol_end = sol[sol_index]

                # Declare current point in solution range
                isValid = False

                # Compare each solution in between
                if sol_start <= start and start <= sol_end: # start point
                    isValid = True
                elif sol_start <= end and end <= sol_end: # end point
                    isValid = True
                elif end < sol_start: # no overlap
                    # Insert to solution
                    sol.insert(sol_index + 1, [start, end])
                    break

                
                # Solution update
                if isValid:

                    # Get new range
                    sol_start = max(sol_start, start)
                    sol_end = min(sol_end, end)
                    
                    # Update solution
                    sol[sol_index] = [sol_start, sol_end]
                    break

                # Update solution index
                sol_index += 1
                
            # Last on the solution list
            if sol_index == len(sol):
                sol.append([start, end])

        # RETURN - length of solution
        return len(sol)