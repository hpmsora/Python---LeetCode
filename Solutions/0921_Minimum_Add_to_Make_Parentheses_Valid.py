class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Declare balance count variable
        b_index = 0
        
        # Declare number of addition
        addition = 0

        # Loop - each letter of string s
        for each_s in s:
            
            # Check letter - open par
            if each_s == "(":
                b_index += 1
            # Check letter - close par
            elif each_s == ")":
                b_index -= 1

                # Check close par not feasible
                if b_index < 0:
                    addition += 1
                    b_index += 1

        # RETURN - conditional
        # 1. Unblanced
        if b_index > 0:
            return b_index + addition
        # 2. Balanced
        else:
            return addition