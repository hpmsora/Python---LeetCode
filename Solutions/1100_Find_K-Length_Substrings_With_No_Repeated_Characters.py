class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        right = k
        sol = 0
        
        if len(s) < k:
            return sol
        
        # init
        freq = {}
        for each_s in s[:k]:
            if each_s in freq:
                freq[each_s] += 1
            else:
                freq[each_s] = 1
                
        if len(freq) == k:
            sol += 1
        left = 0
        
        while right < len(s):
            prev_letter = s[left]
            new_letter = s[right]
            
            if prev_letter == new_letter:
                pass
            else:
                if freq[prev_letter] == 1:
                    del freq[prev_letter]
                else:
                    freq[prev_letter] -= 1
                if new_letter in freq:
                    freq[new_letter] += 1
                else:
                    freq[new_letter] = 1
            
            if len(freq) == k:
                sol += 1
            left += 1
            right += 1
        return sol