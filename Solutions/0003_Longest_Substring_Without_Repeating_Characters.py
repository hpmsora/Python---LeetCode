class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        first = 0
        second = first
        inside = set([s[first]])

        sol = 1

        while second < len(s) - 1:
            second += 1
            curr_letter = s[second]

            while curr_letter in inside:
                inside.remove(s[first])
                first += 1
            inside.add(curr_letter)

            sol = max(sol, second - first + 1)
        return sol