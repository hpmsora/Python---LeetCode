class Solution:
    def minChanges(self, s: str) -> int:
        prev_s = s[0]
        count = 1
        sol = 0
        isSwap = False
        for each_s in s[1:] + "=":
            if each_s == prev_s:
                count += 1
            elif each_s == "=":
                if count % 2 == 1:
                    if not isSwap:
                        isSwap = True
                    else:
                        sol += 1
                        isSwap = False
                else:
                    if isSwap:
                        sol += 1
            else:
                prev_s = each_s

                if count % 2 == 1:
                    if not isSwap:
                        isSwap = True
                    else:
                        sol += 1
                        isSwap = False
                else:
                    if isSwap:
                        sol += 1

                count = 1
        return sol