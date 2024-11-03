class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Loop - index of string s
        for index in range(len(s)):
            # Check the goal string can be made
            if goal == (s[index:]+s[:index]):
                # RETURN - Feasible solution
                return True
        # RETURN - Not-feasible solution
        return False