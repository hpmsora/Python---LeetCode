class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        s1_list_letter_freq = {}
        
        for each_s1 in s1:
            if each_s1 in s1_list_letter_freq:
                s1_list_letter_freq[each_s1] += 1
            else:
                s1_list_letter_freq[each_s1] = 1
        
        # init
        right = len(s1)
        curr_dict = {}
        for index in range(right):
            if s2[index] in curr_dict:
                curr_dict[s2[index]] += 1
            else:
                curr_dict[s2[index]] = 1
                
        def check_per(_curr_dict, _target):
            for letter, freq in _target.items():
                if not letter in _curr_dict:
                    return False
                elif not freq == _curr_dict[letter]:
                    return False
            return True
        
        # init Check
        if check_per(curr_dict, s1_list_letter_freq):
            return True
        
        # Rest
        for index in range(right, len(s2)):
            right_letter = s2[index]
            if right_letter in curr_dict:
                curr_dict[right_letter] += 1
            else:
                curr_dict[right_letter] = 1
                
            earliest_letter = s2[index-len(s1)]

            if curr_dict[earliest_letter] == 1:
                del curr_dict[earliest_letter]
            else:
                curr_dict[earliest_letter] -= 1
            if check_per(curr_dict, s1_list_letter_freq):
                return True
        return False