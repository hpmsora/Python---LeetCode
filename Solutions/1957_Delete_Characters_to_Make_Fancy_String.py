class Solution:
    def makeFancyString(self, s: str) -> str:
        index = 1

        sol = s[0]
        prev_letter = s[0]
        dup_count = 1
        while index < len(s):
            curr_letter = s[index]

            if curr_letter == prev_letter:
                dup_count += 1
                if dup_count > 2:
                    index += 1
                    continue
                index += 1
                sol += curr_letter
            else:
                prev_letter = curr_letter
                dup_count = 1
                index += 1
                sol += curr_letter
        return sol