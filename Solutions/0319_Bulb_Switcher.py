class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        
        index = 1
        sol = 0
        
        while index**2 <= n:
            sol += 1
            index += 1
            
        return sol