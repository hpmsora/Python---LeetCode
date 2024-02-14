class Solution:
    def removeDuplicates(self, s: str) -> str:
        sol = []
        for each_s in s:
            if not sol:
                sol.append(each_s)
                continue

            if sol[-1] == each_s:
                sol.pop()
            else:
                sol.append(each_s)
        
        return ''.join(sol)