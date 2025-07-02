class Solution:
    def possibleStringCount(self, word: str) -> int:
        sol = 1

        prev_letter = word[0]
        temp_sol = 1

        for letter in word[1:]:
            if prev_letter == letter:
                temp_sol += 1
            else:
                sol += temp_sol - 1
                prev_letter = letter
                temp_sol = 1
        
        sol += temp_sol - 1

        return sol