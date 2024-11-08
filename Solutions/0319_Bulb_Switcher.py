class Solution:
    def bulbSwitch(self, n: int) -> int:
        sol = 0
        
        count = 1
        
        while count*count <= n:
            sol += 1
            count += 1
        return sol