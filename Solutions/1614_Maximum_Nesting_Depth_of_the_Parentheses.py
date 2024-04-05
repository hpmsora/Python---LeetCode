class Solution:
    def maxDepth(self, s: str) -> int:
        sol = 0

        new_depth = 0

        for each_s in s:
            if each_s == "(":
                new_depth += 1
                if new_depth > sol:
                    sol = new_depth
            elif each_s == ")":
                new_depth -= 1
    
        return sol