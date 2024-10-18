class Solution:
    def minLength(self, s: str) -> int:
        s = list(s)
        removed_letter = 0

        prev_removed_letter = -1
        while not removed_letter == prev_removed_letter:
            prev_removed_letter = removed_letter
            for index in range(len(s) - 1):
                if s[index] == "0":
                    continue
                if s[index] == "A":
                    index_2 = index + 1
                    while index_2 < len(s):
                        if s[index_2] == "0":
                            index_2 +=1
                            continue
                        elif s[index_2] == "B":
                            s[index] = "0"
                            s[index_2] = "0"
                            removed_letter += 2
                            break
                        else:
                            break
                        index_2 +=1
                elif s[index] == "C":
                    index_2 = index + 1
                    while index_2 < len(s):
                        if s[index_2] == "0":
                            index_2 +=1
                            continue
                        elif s[index_2] == "D":
                            s[index] = "0"
                            s[index_2] = "0"
                            removed_letter += 2
                            break
                        else:
                            break
                        index_2 +=1
        return len(s) - removed_letter