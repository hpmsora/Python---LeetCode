class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # parentheses reserve count
        p_count = 0

        # solution count
        sol = 0

        # Loop - each character list
        for each_s in s:
            if each_s == ")": # letter is close parentheses
                if p_count > 0: # parentheses open exist
                    p_count -= 1 # parentheses open remove once
                else: # parentheses open not exist
                    sol += 1 # removing list update
            else:
                p_count += 1 # parentheses open add one
        
        # RETURN: removed parentheses count + still open parenthese count
        return sol + p_count