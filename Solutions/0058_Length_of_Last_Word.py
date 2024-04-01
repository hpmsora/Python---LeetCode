class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # index variable for count position
        index = 0

        # word length
        sol = 0

        # loop - check each letter
        while index < len(s):
            if s[len(s) - index - 1] == " ": # check the letter is space
                if not sol == 0: # check solution is empty
                    # RETURN - length of current solution
                    return sol
            else: # otherwise
                sol += 1
            
            # update index
            index += 1
            
        # RETURN - end of s
        return sol