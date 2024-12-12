class Solution:
    def maximumLength(self, s: str) -> int:
        letter_freq = {}
        sol = -1

        for index, each_s in enumerate(s):
            if each_s in letter_freq:
                letter_freq[each_s] += 1
                if letter_freq[each_s] >=3:
                    sol = max(1, sol)
            else:
                letter_freq[each_s] = 1

            index -= 1
            new_s = each_s
            while index >= 0:
                if each_s == s[index]:
                    new_s += each_s
                    if new_s in letter_freq:
                        letter_freq[new_s] += 1
                        if letter_freq[new_s] >= 3:
                            sol = max(sol, len(new_s))
                    else:
                        letter_freq[new_s] = 1
                else:
                    break
                index -= 1
        return sol