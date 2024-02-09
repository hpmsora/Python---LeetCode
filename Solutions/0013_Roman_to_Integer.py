class Solution:
    def romanToInt(self, s: str) -> int:
        # r_num_dict
        r_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        # variables:
        sol = 0
        prev = float('inf')
        
        # Loop - each s
        for each_s in s:
            num = r_dict[each_s]
            if num > prev: # speical case
                sol += num - prev*2
            else: # normal case
                sol += num
            
            # update prev
            prev = num
        
        return sol