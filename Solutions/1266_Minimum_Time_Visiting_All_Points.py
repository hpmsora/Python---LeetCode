class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        sol = 0
        
        for point in points[1:]:
            x, y = point
            prev_x, prev_y = prev
            
            delta_x = abs(prev_x - x)
            delta_y = abs(prev_y - y)
            
            min_dia = min(delta_x, delta_y)
            move = max(delta_x - min_dia, delta_y - min_dia)
            
            sol += min_dia + move
            
            prev = point
        
        return sol