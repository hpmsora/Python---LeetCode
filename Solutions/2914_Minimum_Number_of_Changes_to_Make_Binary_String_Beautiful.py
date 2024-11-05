class Solution:
    def minChanges(self, s: str) -> int:
        num_sequece_list = []

        prev_s = s[0]
        count = 1
        for each_s in s[1:] + "=":
            if each_s == prev_s:
                count += 1
            elif each_s == "=":
                num_sequece_list.append(count)
            else:
                num_sequece_list.append(count)
                prev_s = each_s
                count = 1
        
        sol = 0
        isSwap = False
        for each_sequence in num_sequece_list:
            if each_sequence % 2 == 1:
                if not isSwap:
                    isSwap = True
                else:
                    sol += 1
                    isSwap = False
            else:
                if isSwap:
                    sol += 1 
        return sol