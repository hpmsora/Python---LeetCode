class Solution:
    def mySqrt(self, x: int) -> int:
        sol = 0

        while sol * sol <= x:
            sol += 1
        
        return sol - 1